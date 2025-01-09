import cv2
import numpy as np

img=cv2.imread(r"media/ucak.png",0)#0 koyunca siyah beyaz gösterir
row,col=img.shape #boyutları aldık

M=np.float32([[1,0,100],[0,1,70]])#x,y düzleminde matrisimi belirledim
#100 xde bıraktığı siyah boşluğu temsil ederken 70 y deki siyah boşluğu temsil eder buna göre kaydırma işlemi gerçekleşir
dst=cv2.warpAffine(img,M,(row,col)) #bu fonk ile istediğim şekilde kaydırabilirim

cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()