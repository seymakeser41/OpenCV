import cv2
import numpy as np

img=cv2.imread(r"media/ucak.png",0)#0 koyunca siyah beyaz gösterir
row,col=img.shape #boyutları aldık

M=cv2.getRotationMatrix2D((col/2,row/2),90,1)#döndürme işlemini yaptık
#satır ve sütünları sayılara bölüp o kesimi 90 derece döndürdü ve 1 yazdığı için aynı gösterdi daha büyük sayılarda yakınlaştırır
dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()