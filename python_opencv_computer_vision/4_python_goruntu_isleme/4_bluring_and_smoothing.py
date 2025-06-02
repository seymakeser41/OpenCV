import cv2
import numpy as np
import matplotlib.pyplot as plt 

#blurring ve smooting işlemleri resimlerde köşeler , kenarlar belirlenirken çok önemlidir.

img=cv2.imread(r"C:\Users\seyma\Desktop\media\duvar.jpg")
img2=cv2.imread(r"C:\Users\seyma\Desktop\media\median.png")
img_gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#parlaklık değiştirmek için gamma değeri pelirlendi ve parlaklık o değer kadar etki etti
gamma=1/4
result=np.power(img,gamma)
#yazı yazdık
img_1=cv2.putText(img, "duvar",(100,100), fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=4,color=(255,0,0),thickness=4)
#blur kullanarak bulanıklaştırdık
blur=cv2.blur(img, ksize=(5,5))
blur2=cv2.medianBlur(img2, 5 )#farklı bir blur fonksiyonu , gürültüyü azalttı


cv2.imshow('resim', img)
cv2.imshow('parlaklik1',result)
cv2.imshow('yazi',img_1)
cv2.imshow('blur', blur)
cv2.imshow('blur2',blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()