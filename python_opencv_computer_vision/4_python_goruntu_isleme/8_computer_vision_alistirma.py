import cv2 
import numpy as np
import matplotlib.pyplot as plt

#1- Media dosyası altındaki bulunan at.jpg adlı fotoğrafı açınız ve jupyter ekranına basınız 
img=cv2.imread(r"C:\Users\seyma\Desktop\media\at.jpg")
#2- Ekrana basılan resmin binaries formata çevrilmesi ve gösterilmesi
img_gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret,th1=cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
#3- Resmi HSV renk uzayına çeviriniz.
img_hsv=cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#4- 4*4 'lük bir filtre oluşturun. Her bir elemanın değeri 1/10(01) olmalıdır. 
# Daha sonra 2D konvolüsyon kullanarak resmi ekrana bastır. 
kernel=np.ones((4,4),np.float32) /10
konv=cv2.filter2D(img, -1, kernel)
#5- Yatay Sobel filtre oluşturun. Resminize uygulanacak kernel size 5 seçiniz. Ardından gradient filtre uygulayarak resmi bastırın.
sobelx=cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
#6- Resmin 3 kanalının histogram grafiğini çıkarın.(R,G,B)
color=('r','g','b')

for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr)
    plt.xlim([0,256])

plt.title('HISTOGRAM')
plt.show()

cv2.imshow('resim', img)
cv2.imshow('gray',img_gray)
cv2.imshow('th1',th1)
cv2.imshow('hsv',img_hsv)
cv2.imshow('konv_2D ', konv)
cv2.imshow('sobel_x', sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()