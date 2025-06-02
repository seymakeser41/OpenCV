import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image#python image library
pic=Image.open(r"C:\Users\seyma\Desktop\media\aircraft.jpg") #resmi aç
pic_array=np.asarray(pic) #resimi arraye çevir
shape_pic=pic_array.shape #resmin boyutlarını öğrendik
plt.imshow(pic_array) #pyplot kullanarak resmi görüntüleme
plt.show()
kirmizi=pic_array[:,:,0]# sadece kırmızı rengi maskeler
plt.imshow(pic_array[:,:,0]) #kırmızı renkli bölgeyi gösterdi ama saıya yakın
plt.show()
gray=plt.imshow(pic_array[:,:,0], cmap='gray')#kırmızı bölgeleri beyazlatır , kanlaı 2 yapınca mavi değerler beyazlar iken 3de yeşiller olur
pic_array[:,:,1]=0 
pic_array[:,:,2]=0 #mavi yeşili sıfırlarsak tamamen kırmızı resim gelir
plt.imshow(pic_array)
plt.show(pic_array)