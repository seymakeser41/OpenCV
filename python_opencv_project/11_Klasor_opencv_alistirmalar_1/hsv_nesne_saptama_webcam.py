import cv2
import numpy as np

def nothing(x):#trackbarlar için gerekli boş fonksiyon
    pass

cap=cv2.VideoCapture(0)#videoyu webcamden aldık
cv2.namedWindow("Trackbar")#tracbar penceresi açıldı
#trackbarları oluşturduk
cv2.createTrackbar("LH","Trackbar",0,179,nothing)
cv2.createTrackbar("LS","Trackbar",0,255,nothing)
cv2.createTrackbar("LV","Trackbar",0,255,nothing)
cv2.createTrackbar("UH","Trackbar",0,179,nothing)
cv2.createTrackbar("US","Trackbar",0,255,nothing)
cv2.createTrackbar("UV","Trackbar",0,255,nothing)

while 1:
    _,frame=cap.read()
    frame=cv2.flip(frame,1)#görüntüyü ters çeviridi
    frame=cv2.resize(frame,(400,300))#boyutlandırdık
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #trackbarlardan değerleri çektik
    lh=cv2.getTrackbarPos("LH","Trackbar")
    ls=cv2.getTrackbarPos("LS","Trackbar")
    lv=cv2.getTrackbarPos("LV","Trackbar")
    uh=cv2.getTrackbarPos("UH","Trackbar")
    us=cv2.getTrackbarPos("US","Trackbar")
    uv=cv2.getTrackbarPos("UV","Trackbar")
    #sınır değerleri dizilerde tuttuk
    lower_blue=np.array([lh,ls,lv])
    upper_blue=np.array([uh,us,uv])
    #maske uyguladık 
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    #uyguladığımız maskede renklerin gözükmesi için bitwise işlemi uyguladık
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("bitwise",bitwise)
    
    if cv2.waitKey(20) & 0xFF ==ord('q'):#video bittikçe kapanacak tekrar çalıştırın
        break
    
cap.release()
cv2.destroyAllWindows()
