#ALISTIRMALAR
#1-Bir resmi notebook ekranında gösteriniz.
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\kus_resmi.jpg")
new=img.copy()

#2_resmi ters çevirip notebook ekranında bastırınız
new=cv2.flip(new,0)

#3- Resminizde belirli bir bölgeyi kare içine alınız
new_i=img.copy()
cv2.rectangle(new_i,(200,10),(400,80),(255,0,0),5)

#4-resimde 3 nokt abelirleyip üçgen çizin ve sonradan bu üçgeni doldurun

neww=img.copy ()
noktalar = np.array([(100, 200), (50, 300), (150, 300)], np.int32)
cv2.polylines(neww,[noktalar],isClosed=True,color=(0,0,255), thickness=3)

neww_i=neww.copy()   
cv2.fillPoly(neww_i,[noktalar],(0,0,255))

#5-mausa sol tıklandıkça daire çizsin
tikla=img.copy()

def daire_ciz(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(tikla,(x,y),100,(0,0,255),10,-1)
cv2.namedWindow("daireler")  
cv2.setMouseCallback("daireler", daire_ciz)
while True:
    cv2.imshow('daireler',tikla)

    if cv2.waitKey(20 ) & 0xFF ==27:
        break


cv2.imshow('resim',img)
cv2.imshow('ters',new)
cv2.imshow('kare',new_i)
cv2.imshow('ucgen',neww)
cv2.imshow('dolu_ucgen',neww_i)

cv2.waitKey(0)
cv2.destroyAllWindows()




 


