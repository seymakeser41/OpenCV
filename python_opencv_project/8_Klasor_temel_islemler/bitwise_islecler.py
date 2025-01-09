import cv2
import numpy as np

img2=cv2.imread(r"media/bitwise_2.png")
img1=cv2.imread(r"media/bitwise_1.png")

import os

if img1 is None or img2 is None:
    print("Dosyalar yüklenemedi. Lütfen dosya yollarını kontrol edin.")


bit_and=cv2.bitwise_and(img1,img2)# bitwise fonksiyonu ile and gerçekleştirildi
bit_or=cv2.bitwise_or(img1,img2)#or mantığıyla birleştirdi
bit_xor=cv2.bitwise_xor(img1,img2)#xor mantığıyşla birleştirdi
bit_not=cv2.bitwise_not(img1)#not mantığıyşla resmi dönüştürdü
bit_not2=cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("bit_and",bit_and)
cv2.imshow("bit_or",bit_or)
cv2.imshow("bit_xor",bit_xor)
cv2.imshow("bit_not1",bit_not)
cv2.imshow("bit_not2",bit_not2)

cv2.waitKey(0)
cv2.desrtoyAllWindows()