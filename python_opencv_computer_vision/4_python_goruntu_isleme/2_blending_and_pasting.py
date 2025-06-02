import cv2
import numpy as np
import matplotlib.pyplot as plt 

#iki resmi birbiri üstünde birleştirme işlemleri

img1=cv2.imread(r"C:\Users\seyma\Desktop\media\kus_resmi.jpg") 
img2=cv2.imread(r"C:\Users\seyma\Desktop\media\balls.jpg")
#karıştırma işlemi için aynı boyutta olması gerekir
img1=cv2.resize(img1,(600,600))
img2=cv2.resize(img2,(600,600))
#belli oranlarla iki resmi birleştirir
blended=cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
#2.resmi daha küçük yapıp ilk resmin üstüne montelemek için küçülttük
img2=cv2.resize(img2,(300,300))

large_img=img1
small_img=img2
#ikinci resim kadar bir bölgeyi seçip eşleştiriyoruz
large_img[0:300,0:300]= small_img

#eğer boyutlandırma yapmak istemezsek direk büyük resimden istediğimiz kadar bir alanı çekebiliriz
roi=img1[0:600,0:600]
roi[0:300,0:300] = small_img


img2_gray=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)# GRAY format
mask=cv2.bitwise_not(img2_gray) #gri tonlamada yaptığı işlemleri tam tersi yapar siyahsa beyaz , beyazsa siyah
mask = mask.astype(np.uint8)
white_backround=np.full((600,600,3),255,dtype=np.uint8)
mask = cv2.resize(mask, (white_backround.shape[1], white_backround.shape[0]))
bk=cv2.bitwise_or(white_backround,white_backround,mask=mask) #maskeye göre birleştirme

cv2.imshow('blend',blended)
cv2.imshow('large_img',large_img)
cv2.imshow('roi_img',roi)
cv2.imshow('img2gray',img2_gray)
cv2.imshow('mask',mask)
cv2.imshow('bk',bk)
cv2.waitKey(0)
cv2.destroyAllWindows()