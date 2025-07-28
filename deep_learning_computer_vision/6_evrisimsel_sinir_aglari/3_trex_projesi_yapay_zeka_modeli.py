import glob  #ilk iki kütüphane dosyalardaki resimlere ulaşmayı sağlayacak
import os
import numpy as np
from keras.models import Sequential #derin çğrenme algoritmasının tasarlanması ve geliştirilmesi
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D #katmanlar
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  #verileri etkiler , etiketlenmiş veriyi eğitilecek hale getirir
from sklearn.model_selection import train_test_split #verileri ayırma
import seaborn as sns  #görselleştirme 

import warnings  #uyarıları kapatacak
warnings.filterwarnings("ignore")

#resimleri yükler 
imgs = glob.glob(r"C:\Users\seyma\Desktop\media\trex_veri/*.png")

ArithmeticError()
#boyutlar belirlendi
width = 125
height = 50

#x ve y değerleri depolanacak 
X = []
Y = []

for img in imgs:
    
    filename = os.path.basename(img) #resmin adını aldı
    label = filename.split("_")[0] #_ işaretine göre resimin adını ayırdı classı bulmak için (down, up)
    im = np.array(Image.open(img).convert("L").resize((width, height))) #boyutlandırdık
    im = im / 255 #normalizasyon
    X.append(im) #resimler eklendi
    Y.append(label) #etiket eklendi
    
X = np.array(X) #array çevirme
X = X.reshape(X.shape[0], width, height, 1) #kaç resim , boyutlar,renk kanalı(siyah-beyaz)

# sns.countplot(Y) #sınıflardan kaç tane var grafikleştirebiliriz

def onehot_labels(values):
    label_encoder = LabelEncoder() #sınıfları sayısal değere çevireceğiz
    integer_encoded = label_encoder.fit_transform(values) #önce ne yapacağını öğreniyor sonra dönüştürüyor, sınıflan numaralandırıldı
    onehot_encoder = OneHotEncoder(sparse_output=False) #sparse matris elde etmeden onehotencoder oluşturur
    integer_encoded = integer_encoded.reshape(len(integer_encoded),1) #boş olan verinin yerine 1 koyarak (veri sayısı,1) şeklinde düzenlendi
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded) #fit, transform yapıldı(öğrendi ve dönüştürüldü)
    return onehot_encoded  #3 sınıfı 3 basamaklı sayısal binary rakamlarla temsil edilen sınıfsal dizi oluştu

Y = onehot_labels(Y)
#veri kümesini ayrıştırma
train_X, test_X, train_y, test_y = train_test_split(X, Y , test_size = 0.25, random_state = 2)   #test veri seti 1/4 oranında  , rastgele bölünme

# cnn model
model = Sequential()   #katmanların üzerine eklenecek temel yapı
model.add(Conv2D(32, kernel_size = (3,3), activation = "relu", input_shape = (width, height, 1))) #32 tane 3*'lük filtre, 
model.add(Conv2D(64, kernel_size = (3,3), activation = "relu"))
model.add(MaxPooling2D(pool_size = (2,2))) #piksel ekleme filtresi
model.add(Dropout(0.25)) #seyreltme
model.add(Flatten())
model.add(Dense(128, activation = "relu")) #gizli katman , 128 nöron
model.add(Dropout(0.4))
model.add(Dense(3, activation = "softmax")) #çıktı katmanı 

#model yükleme 
weight_path = "C:/Users/seyma/Desktop/opencv_bolumu/deep_learning_computer_vision/model/trex_weight.h5"

if os.path.exists(weight_path):
    model.load_weights(weight_path)
    print("Weights yüklendi")
else:
    print("Weights dosyasi bulunamadi!")

model.compile(loss = "categorical_crossentropy", optimizer = "Adam", metrics = ["accuracy"]) #kayıp, parametre optimize, metrik(doğruluk)

model.fit(train_X, train_y, epochs = 35, batch_size = 64) #35 kez eğitim ve 64erli gruplar halinde giriş 

#train doğruluk 
score_train = model.evaluate(train_X, train_y)
print("Eğitim doğruluğu: %",score_train[1]*100)    #ilk veri kayıp , ikinci veri doğruluk

#test doğruluk
score_test = model.evaluate(test_X, test_y)
print("Test doğruluğu: %",score_test[1]*100)      
    
# sonuçları kaydetme
open("model_new.json","w").write(model.to_json())
model.save_weights("trex_weight_new.weights.h5")   
