import cv2
import numpy as np

cap=cv2.VideoCapture(r"media/dog.mp4")

while 1:
    _,frame=cap.read()#bir doğru yanlış değeri birde frameleri çektik
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #beyaz nesneyi ayırmak için alt ve üst değer girmemiz gerek
    sensitivity=15 #hsv code for whitw diyerek ulaşabiliriz
    lower_white=np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    mask=cv2.inRange(hsv,lower_white,upper_white) #değerler arasınada maskeleme işlemi yaptık
    res=cv2.bitwise_and(frame,frame,mask=mask)# maskeleme işlemi için gereklidir bir orjinal bir kazıdığımız resim olduğundan iki tane frame girmek gerekir

    cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k=cv2.waitKey(5)&0xFF #esc ye basınca duracak
    if k ==27:
        break

cv2.destroyAllWindows()