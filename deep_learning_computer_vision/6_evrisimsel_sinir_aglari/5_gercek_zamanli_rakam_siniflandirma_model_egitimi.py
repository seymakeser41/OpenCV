
import numpy as np
import cv2
import os#veri içeri aktarma
from sklearn.model_selection import train_test_split  #veri ayırma
from sklearn.metrics import confusion_matrix
import seaborn as sns#görselleştirme
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential#model temeli
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout #katmanlar
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pickle #model yükleme

#veriler
path = r"C:\Users\seyma\Desktop\media\myData"

myList = os.listdir(path)#yoldaki verileri listeleme 10 klasör
noOfClasses = len(myList) #mylist uzunluğu 

print("Label(sinif) sayisi: ",noOfClasses)


images = []
classNo = []

for i in range(noOfClasses):
    myImageList = os.listdir(path + "\\"+str(i)) #klasörlerde gezer
    for j in myImageList:
        img = cv2.imread(path + "\\" + str(i) + "\\" + j) #klasördeki resimlerde gezer
        img = cv2.resize(img, (32,32)) #boyutlandırma
        images.append(img)
        classNo.append(i)
        
print(len(images)) #kaç resim 
print(len(classNo))

#diziye çevir
images = np.array(images)
classNo = np.array(classNo)

#boyutlar
print(images.shape) #(10160, 32,32,3)
print(classNo.shape) #(10160,)

# veriyi ayırma
x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size = 0.5, random_state = 42) #train ve test ayrımı
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size = 0.2, random_state = 42) #train ve validation

print(images.shape) #(10160, 32, 32,3)
print(x_train.shape) #(4064), 32, 32,3)
print(x_test.shape)  #(5080, 32, 32,3)
print(x_validation.shape) #(1016, 32, 32,3)

# # görselleştirme (dağılımı görmek için)
# fig, axes = plt.subplots(3,1,figsize=(7,7))
# fig.subplots_adjust(hspace = 0.5)
# sns.countplot(y_train, ax = axes[0])
# axes[0].set_title("y_train")

# sns.countplot(y_test, ax = axes[1])
# axes[1].set_title("y_test")

# sns.countplot(y_validation, ax = axes[2])
# axes[2].set_title("y_validation")

# preprocess
def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray dönüşümü
    img = cv2.equalizeHist(img) #histogram genişletildi
    img = img /255 #normalizasyon
    
    return img


#deneme amaçlı resimleri görselleştirme
# idx = 311
# img = preProcess(x_train[idx])
# img = cv2.resize(img,(300,300))
# cv2.imshow("Preprocess ",img)

#map ile fonksiyonu tüm verilere uyguladık    
x_train = np.array(list(map(preProcess, x_train)))
x_test = np.array(list(map(preProcess, x_test)))
x_validation = np.array(list(map(preProcess, x_validation)))

#verilerin boyutu eğitim içim ayarlandı
x_train = x_train.reshape(-1,32,32,1) #-1 :boyut neyse onu al diğer parametreleri girilen değere göre ayarla
print(x_train.shape)
x_test = x_test.reshape(-1,32,32,1)
x_validation = x_validation.reshape(-1,32,32,1)

# data generate
dataGen = ImageDataGenerator(width_shift_range = 0.1, #0.1 oranında kaydır
                             height_shift_range = 0.1,
                             zoom_range = 0.1,
                             rotation_range = 10)

dataGen.fit(x_train) #uygulandı

#keras için gerekli kategorik dönüşüm
y_train = to_categorical(y_train, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)

#modeli oluşturma
model = Sequential()
model.add(Conv2D(input_shape = (32,32,1), filters = 8, kernel_size = (5,5), activation = "relu", padding = "same")) 
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D( filters = 16, kernel_size = (3,3), activation = "relu", padding = "same"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(units=256, activation = "relu" ))
model.add(Dropout(0.2))
model.add(Dense(units=noOfClasses, activation = "softmax" ))

model.compile(loss = "categorical_crossentropy", optimizer=("Adam"), metrics = ["accuracy"])

batch_size = 250

# model çıktısını görüntüleme
hist = model.fit(dataGen.flow(x_train, y_train, batch_size = batch_size),
                 validation_data = (x_test, y_test),
                 epochs = 15,
                 steps_per_epoch = x_train.shape[0] // batch_size,
                 shuffle = True)

pickle_out = open("model_trained_new.p","wb") #modeli içine depolayacak
pickle.dump(model, pickle_out)
pickle_out.close()

# %% degerlendirme
hist.history.keys()


plt.figure()
plt.plot(hist.history["loss"], label = "Eğitim Loss")
plt.plot(hist.history["val_loss"], label = "Val Loss")
plt.legend()
plt.show()

plt.figure()
plt.plot(hist.history["accuracy"], label = "Eğitim accuracy")
plt.plot(hist.history["val_accuracy"], label = "Val accuracy")
plt.legend()
plt.show()

#sonuç
score = model.evaluate(x_test, y_test, verbose = 1)
print("Test loss: ", score[0])
print("Test accuracy: ", score[1])


y_pred = model.predict(x_validation) #tahmin
y_pred_class = np.argmax(y_pred, axis = 1)
Y_true = np.argmax(y_validation, axis = 1) #gerçek değer
cm = confusion_matrix(Y_true, y_pred_class) #karşılaştırma
f, ax = plt.subplots(figsize=(8,8))
#confusion_matrix görselleştirme
sns.heatmap(cm, annot = True, linewidths = 0.01, cmap = "Greens", linecolor = "gray", fmt = ".1f", ax=ax)
plt.xlabel("predicted")
plt.ylabel("true")
plt.title("cm")
plt.show()