import cv2
import numpy as np

img=cv2.imread(r"media/contour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #threshold işlemi yaptık
M=cv2.moments(thresh)# key ve valuelerden oluşan kütüphane şeklinde momentleri tutar
#ağırlık merkezini bulmak için belirli noktalar bulmalıyız
X= int(M["m10"]/M["m00"])
Y= int(M["m01"]/M["m00"])
cv2.circle(img,(X,Y),5,(0,255,0),-1) # merkeze bir daire çizdik

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=contours[0] #contourların ilk değeriyle alan hesaplayacağız
area=cv2.contourArea(cnt)
print(area)

M1=cv2.moments(cnt)#M1["m00] değeri de alanı verir
print(M1['m00'])

perimeter=cv2.arcLength(cnt,True) #çevreyi hesaplayan fonksiyon true kapalı bir şekilse çevreyi hesaplıcak
print(perimeter)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()