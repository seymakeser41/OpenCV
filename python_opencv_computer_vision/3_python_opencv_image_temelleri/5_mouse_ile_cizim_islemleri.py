import cv2
import numpy as np 

img=np.zeros((512,512,3),dtype=np.uint8)#boş siyah ekran

def daire_ciz(event,x,y,flags,param):#daire çizen fonksiyon
    if event==cv2.EVENT_LBUTTONDOWN:#sol click olayı gelirse yeşil daire çizer
        cv2.circle(img,(x,y),100,(0,0,255),-1)

    elif event==cv2.EVENT_RBUTTONDOWN:#sağ click olayı gelirse kırmızı renk çizer
        cv2.circle(img,(x,y),100,(255,0,0),-1)


cv2.namedWindow(winname='deneme') #göstermek için pencere açtık
cv2.setMouseCallback('deneme',daire_ciz)#maustan basıldıkça fonksiyonu çağırdık

#esc'ye basana kadar görüntüledik
while True:
    cv2.imshow('deneme',img)

    if cv2.waitKey(20) & 0xFF ==27:
        break

