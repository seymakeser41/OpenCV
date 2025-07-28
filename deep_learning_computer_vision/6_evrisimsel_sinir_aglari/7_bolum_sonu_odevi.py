import numpy as np
import cv2
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Fruit360 veri yolu
path = r"C:\Users\seyma\Downloads\archive\fruits-360_100x100\fruits-360\Training"
classNames = os.listdir(path)
noOfClasses = len(classNames)

print("Sınıf Sayısı:", noOfClasses)

images = []
classNo = []

for index, folderName in enumerate(classNames):
    folderPath = os.path.join(path, folderName)
    imageList = os.listdir(folderPath)
    
    for imageName in imageList:
        imgPath = os.path.join(folderPath, imageName)
        img = cv2.imread(imgPath)
        if img is not None:
            img = cv2.resize(img, (32, 32))
            images.append(img)
            classNo.append(index)

print("Toplam Görsel:", len(images))
print("Toplam Etiket:", len(classNo))

# numpy dizilerine çevir
images = np.array(images)
classNo = np.array(classNo)

# veri ayırma
x_train, x_test, y_train, y_test = train_test_split(images, classNo, test_size=0.2, random_state=42)
x_train, x_validation, y_train, y_validation = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

# ön işleme fonksiyonu
def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255.0
    return img

# preprocess tüm verilere uygulanıyor
x_train = np.array([preProcess(img) for img in x_train])
x_test = np.array([preProcess(img) for img in x_test])
x_validation = np.array([preProcess(img) for img in x_validation])

# model girişi için reshape
x_train = x_train.reshape(-1, 32, 32, 1)
x_test = x_test.reshape(-1, 32, 32, 1)
x_validation = x_validation.reshape(-1, 32, 32, 1)

# label'ları one-hot kategorik yap
y_train = to_categorical(y_train, noOfClasses)
y_test = to_categorical(y_test, noOfClasses)
y_validation = to_categorical(y_validation, noOfClasses)

# veri arttırma
dataGen = ImageDataGenerator(width_shift_range=0.1,
                             height_shift_range=0.1,
                             zoom_range=0.1,
                             rotation_range=10)
dataGen.fit(x_train)

# model tanımı
model = Sequential([
    Conv2D(8, (5,5), activation='relu', padding='same', input_shape=(32,32,1)),
    MaxPooling2D((2,2)),
    Conv2D(16, (3,3), activation='relu', padding='same'),
    MaxPooling2D((2,2)),
    Dropout(0.2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.2),
    Dense(noOfClasses, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# eğitim
hist = model.fit(dataGen.flow(x_train, y_train, batch_size=256),
                 validation_data=(x_test, y_test),
                 epochs=15,
                 steps_per_epoch=len(x_train)//256,
                 shuffle=True)

# modeli pickle ile kaydet
with open("fruit360_model.p", "wb") as f:
    pickle.dump(model, f)

# sonuçlar
plt.plot(hist.history["loss"], label="Train Loss")
plt.plot(hist.history["val_loss"], label="Val Loss")
plt.legend()
plt.show()

plt.plot(hist.history["accuracy"], label="Train Acc")
plt.plot(hist.history["val_accuracy"], label="Val Acc")
plt.legend()
plt.show()

score = model.evaluate(x_test, y_test)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
