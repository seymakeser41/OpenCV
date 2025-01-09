import cv2
import numpy as np

def nothing(x):#tracbar i�in bo� fonksiyon
    pass

cap =cv2.VideoCapture(0)
cv2.namedWindow("settings")
#tracbarlar� olu�turduk
cv2.createTrackbar("lower-hue", "settings",0,180,nothing)
cv2.createTrackbar("lower-saturation", "settings",0,255,nothing)
cv2.createTrackbar("lower-value", "settings",0,255,nothing)
cv2.createTrackbar("upper-hue", "settings",0,180,nothing)
cv2.createTrackbar("upper-saturation", "settings",0,255,nothing)
cv2.createTrackbar("upper-value", "settings",0,255,nothing)

font=cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)#g�r�nt�y� ters �evirdi
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #tracbardaki de�erleri ald�k
    lh=cv2.getTrackbarPos("lower-hue","settings")
    ls=cv2.getTrackbarPos("lower-saturation","settings")
    lv=cv2.getTrackbarPos("lower-value","settings")
    uh=cv2.getTrackbarPos("upper-hue","settings")
    us=cv2.getTrackbarPos("upper-saturation","settings")
    uv=cv2.getTrackbarPos("upper-value","settings")

    lower_color=np.array([lh,ls,lv]) #de�erler kullan�larak color de�eri bulundu
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)#maskeledik
    kernel=np.ones((5,5),np.uint8)#olu�an siyah noktalar� yok etmek i�in
    mask=cv2.erode(mask,kernel) #farkl� bir maske uygulad�k

    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #contourlar� �ektik

    for cnt in contours:#contourlar� kullanarak bir merkez ve alan hesaplan�r 
        area=cv2.contourArea(cnt)
        epsilon=0.02*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)

        x=approx.ravel()[0]#contourlar�m�z�n ba�lad��� de�er
        y=approx.ravel()[1]

        if area>400:#e�er 400 den b�y�kse bir �ey �izebilir
            cv2.drawContours(frame,[approx],0,(0,0,0),5)
            if len(approx)==3:
                cv2.putText(frame,"triangle",(x,y),font,1,(0,0,0))
            elif len(approx)==4:
                cv2.putText(frame,"rectangle",(x,y),font,1,(0,0,0))
            elif len(approx)==5:
                cv2.putText(frame,"pentagon",(x,y),font,1,(0,0,0))
            if len(approx)>6:
                cv2.putText(frame,"circle",(x,y),font,1,(0,0,0))

    
                
                
                
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(3) &0xFF==ord("q"):

        break

    cv2.waitKey(0)
    cv2.destroyAllWindows()



