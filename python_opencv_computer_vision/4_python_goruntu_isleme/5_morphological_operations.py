import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((600,600),dtype=np.uint8)
img=cv2.putText(img,"ABCDE",(50,300),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=5,color=(255,255,255),thickness=20)

kernel=np.ones((5,5),dtype=np.uint8)
#erode işlemi gürültüleri azaltır , inceltir
result=cv2.erode(img,kernel, iterations=2)

white_noise=np.random.randint(low=0,high=2, size=(600,600),dtype=np.uint8)
white_noise=white_noise * 255

noise_img=white_noise + img

morph=cv2.morphologyEx(noise_img,cv2.MORPH_OPEN, kernel)

# img de int16 yapılmalı ki negatifle toplama doğru çalışsın
img_int = img.astype(np.int16)
#harflerin içerisini gürültüyle doldurma
black_noise=np.random.randint(low=0,high=2,size=(600,600),dtype=np.int16)
black_noise=black_noise * -255

black_noise_img= black_noise + img_int

black_noise_img[black_noise_img==-255]=0

# Gürültü olan (negatif) pikselleri sıfıra eşitle
#black_noise_img[black_noise_img < 0] = 0

# Görüntüyü tekrar uint8’e çevir
black_noise_img = black_noise_img.astype(np.uint8)

#harf içerisindeki görültüleri temizler
morph2= cv2.morphologyEx(black_noise_img,cv2.MORPH_CLOSE, kernel)
#belirli kenarların içerisini boşaltır
morph3=cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('resim',img)
cv2.imshow('erode',result)
cv2.imshow('white_noise',white_noise)
cv2.imshow('noise_img', noise_img)
cv2.imshow('morph', morph)
cv2.imshow('blac_noise_img', black_noise_img)
cv2.imshow('morph2', morph2)
cv2.imshow('morph3', morph3)

cv2.waitKey(0)
cv2.destroyAllWindows()

