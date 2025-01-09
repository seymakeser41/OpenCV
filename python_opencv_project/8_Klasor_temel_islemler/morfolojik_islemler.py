from os import close

import cv2
import numpy as np

img=cv2.imread(r"media/ucak2.jpg",0)
kernel=np.ones((5,5),np.uint8)#erezyon işlemi için 5e 5lik birim matrisi oluşturduk
erosion=cv2.erode(img,kernel,iterations=1)#erezyon işlemini yaptık , bozulmalar oldu,inceliyor
dilation=cv2.dilate(img,kernel,iterations=3)#kalınlaştırma işlemi yapıyor
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)#resmin üzerindeki gürültüyü gereksiz noktaları kaldırır
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)#resmin içindeki uyumsuzluklar giderilmiş
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)#resmin dışını beyaz çizer kalanı siyah
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)#resimdeki kesişimleri kararttı

cv2.imshow("img",img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("gradient",gradient)
cv2.imshow("tophat",tophat)
cv2.waitKey(0)
cv2.destroyAllWindows()