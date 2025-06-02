import cv2 
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\gradients.jpg", 0)

#x gradient uygulanarak dikey eksendeki çizgiler daha belirgin yatay eksendeki çizgiler daha siliktir.
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0, ksize=5)
#y gradient uygulanarak yatay eksendeki çizgiler daha belirgin dikey eksendeki çizgiler daha siliktir.
sobely=cv2.Sobel(img,cv2.CV_64F,0,1, ksize=5)
#hem yatay yem dikey olarak gradient uygulamak laplacian işlemidir
laplacian=cv2.Laplacian(img, cv2.CV_64F)
#iki gradient işlemini birleştirdiğimiz için daha belirgin bir sonuç elde ederiz
toplam=cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#50 değeri üzerinden threshold işlemi uyguladık
ret,th1=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
#morphology işlemi için kullanılacak kernel oluşturduk
kernel=np.ones((4,4),np.uint8)
#morphology işlemi uyguladık
morph1=cv2.morphologyEx(toplam, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('resim', img)
cv2.imshow('x_gradient', sobelx)
cv2.imshow('y_gradient', sobely)
cv2.imshow('laplacian', laplacian)
cv2.imshow('birlesim', toplam)
cv2.imshow('th1',th1)
cv2.imshow('morph1',morph1)
cv2.waitKey(0)
cv2.destroyAllWindows()