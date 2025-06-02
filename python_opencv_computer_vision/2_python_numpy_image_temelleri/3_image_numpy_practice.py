#numpy import et 
import numpy as np
# her elemanı 10 sayısından oluşan 5*5 bir array oluştur
ten_array=np.ones((5,5))* 10

#rastgele sayı üreten hücreyi çalıştır ve gözlemle 
np. random.seed(101)
arr=np.random.randint(low=0,high=100,size=(5,5))

#arrayin en küçük ve en büyük değerlerini bul
max_array=arr.max()
min_array=arr.min()

#göster 
import matplotlib.pyplot as plt
from PIL import Image
pic=Image.open(r"C:\Users\seyma\Desktop\media\aircraft.jpg")
plt.imshow(pic)
plt.show()

#fotoğrafın numpy array olarak dönüşümü sağla ve tip,şekil kontrolu sağla
print(type(pic))
arr_pic=np.asarray(pic)
print(type(arr_pic))
print(arr_pic.shape)
plt.imshow(arr_pic)
plt.show()

#kopyasının üzerinden sadece mavi kanalı göster 
copy=arr_pic.copy()
copy[:,:,0]=0
copy[:,:,1]=0
plt.imshow(copy)
plt.show()