#RESİM YUMUŞATMA

import cv2
import numpy as np

img_filter=cv2.imread(r"media/filter.png")
img_median=cv2.imread(r"media/median.png")
img_bilateral=cv2.imread(r"media/bilateral.png")

blur= cv2.blur(img_filter,(5,5))#blur fonksiyonu ile filtreledik, pozitif tek sayı olmak zorunda
blur_g=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)#Başka bir blur modeli uyguladık

blur_m=cv2.medianBlur(img_median,5)

blur_b=cv2.bilateralFilter(img_bilateral,9,75,75)

cv2.imshow("original",img_filter)
cv2.imshow("blur",blur)
cv2.imshow("blur2",blur_g)
cv2.imshow("original_m",img_median)
cv2.imshow("blur_m",blur_m)
cv2.imshow("original_b",img_bilateral)
cv2.imshow("blur_b",blur_b)



cv2.waitKey(0)
cv2.destroyAllWimdows()
