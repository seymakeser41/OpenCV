#gerekli kütüphaneleri import ettik
import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image
import cv2
pic=Image.open(r"C:\Users\seyma\Desktop\media\aircraft.jpg")
img=cv2.imread(r"C:\Users\seyma\Desktop\media\aircraft.jpg") 
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #RGBye çevirdi
gri=cv2.imread(r"C:\Users\seyma\Desktop\media\aircraft.jpg",cv2.IMREAD_GRAYSCALE)
new_rsz=cv2.resize(img,(600,400))#boyutlandırdı
n_rsz=cv2.resize(img,(0,0),img,0.5,0.5)#oranla boyutlandırdı
ters_x=cv2.flip(img,0)#x e göre ters döndü
ters_y=cv2.flip(img,1) #y ye göre ters döndü
ters=cv2.flip(img,-1) #ters döndü

cv2.imwrite('yeni_resim',img) #kaydetme #yeni resim yazan yere path koyun
#görüntüleme
plt.imshow(img)
plt.show()
plt.imshow(gri,cmap='gray')
plt.show()
plt.imshow(gri,cmap='magma')
plt.show()
cv2.imshow('resim',img)
cv2.imshow('resim2',rgb)
cv2.imshow('gri',gri)
cv2.imshow('rsz',new_rsz)
cv2.imshow('oran_rsz',n_rsz)
cv2.imshow('Ters_x',ters_x)
cv2.imshow('Ters_y',ters_y)
cv2.imshow('Ters',ters)
cv2.waitKey(0)
cv2.destroyAllWindows()