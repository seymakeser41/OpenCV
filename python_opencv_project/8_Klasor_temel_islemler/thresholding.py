import cv2
import numpy as np

img=cv2.imread(r"media/ucak2.jpg",0)#0 koyunca siyah beyaz gösterir
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#threshold işlemi uygalayıp belirtilen yeri koyulaştırıyor
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
#farklı bir threshold modeli uyguladı
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

cv2.imshow("img",img)
cv2.imshow("img_th1",th1)
cv2.imshow("img_th2",th2)
cv2.imshow("img_th3",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
