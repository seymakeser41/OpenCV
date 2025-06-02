import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\kus_resmi.jpg") 
img2=cv2.imread(r"C:\Users\seyma\Desktop\media\ocean_day.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img2_gray=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)


#127 değerinden büyük olan pikselleri siyah diğerlerini beyaz yapar 
ret,thresh1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
# yukardaki matığın tam tersini yapar 
ret1,thresh2=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY_INV)
#farklı threshold yapma yolları vardır , resmimize göre bunlar denenerek en uygunu seçilmelidir
ret2,thresh3=cv2.threshold(img2_gray,127,255,cv2.THRESH_BINARY)
th3=cv2.adaptiveThreshold(img2_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
th4=cv2.adaptiveThreshold(img2_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,8)


cv2.imshow('threshold',thresh1)
cv2.imshow('threshold2',thresh2)
cv2.imshow('threshold3',thresh3)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
