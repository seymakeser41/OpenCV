import cv2
import numpy as np

def nothing(x):#tracbar için boþ fonksiyon
    pass

cap =cv2.VideoCapture(0)
cv2.namedWindow("settings")
#tracbarlarý oluþturduk
cv2.createTrackbar("lower-hue", "settings",0,180,nothing)
cv2.createTrackbar("lower-saturation", "settings",0,255,nothing)
cv2.createTrackbar("lower-value", "settings",0,255,nothing)
cv2.createTrackbar("upper-hue", "settings",0,180,nothing)
cv2.createTrackbar("upper-saturation", "settings",0,255,nothing)
cv2.createTrackbar("upper-value", "settings",0,255,nothing)

font=cv2.FONT_HERSHEY_SIMPLEX

while 1:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)#görüntüyü ters çevirdi
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #tracbardaki deðerleri aldýk
    lh=cv2.getTrackbarPos("lower-hue","settings")
    ls=cv2.getTrackbarPos("lower-saturation","settings")
    lv=cv2.getTrackbarPos("lower-value","settings")
    uh=cv2.getTrackbarPos("upper-hue","settings")
    us=cv2.getTrackbarPos("upper-saturation","settings")
    uv=cv2.getTrackbarPos("upper-value","settings")

    lower_color=np.array([lh,ls,lv]) #deðerler kullanýlarak color deðeri bulundu
    upper_color=np.array([uh,us,uv])

    mask=cv2.inRange(hsv,lower_color,upper_color)#maskeledik
    kernel=np.ones((5,5),np.uint8)#oluþan siyah noktalarý yok etmek için
    mask=cv2.erode(mask,kernel) #farklý bir maske uyguladýk

    contours,_=cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #contourlarý çektik

    for cnt in contours:#contourlarý kullanarak bir merkez ve alan hesaplanýr 
        area=cv2.contourArea(cnt)
        epsilon=0.02*cv2.arcLength(cnt,True)
        approx=cv2.approxPolyDP(cnt,epsilon,True)

        x=approx.ravel()[0]#contourlarýmýzýn baþladýðý deðer
        y=approx.ravel()[1]

        if area>400:#eðer 400 den büyükse bir þey çizebilir
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



