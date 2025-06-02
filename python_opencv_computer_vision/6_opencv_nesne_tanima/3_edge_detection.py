import cv2
import numpy as np
import matplotlib.pyplot as plt
#rsimler yüklenir
img=cv2.imread(r"C:\Users\seyma\Desktop\media\kopek_face.jpg")
#orjinal resim üzerine kenarlar bulunur ama detaylar çok fazla olduğu için istediğimiz sonuca ulaşamayız 
edges=cv2.Canny(img, threshold1=127,  threshold2=127)
#blur fonksiyonuyla bulanıklaştırılıp tekrar kenarlar algılanır ve daha uygun bir sonuç bulunur
blur=cv2.blur(img, ksize=(5,5))
#edges fonksiyonundaki threshold fonksiyonları değiştirilerek istenen sonuca yakınlaşılır
edges_1=cv2.Canny(blur, threshold1=100,  threshold2=180)        

#görselleştirmeler
cv2.imshow('kopek', img)
cv2.imshow('kenar', edges)
cv2.imshow('blur', blur)
cv2.imshow('kenar_1', edges_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

