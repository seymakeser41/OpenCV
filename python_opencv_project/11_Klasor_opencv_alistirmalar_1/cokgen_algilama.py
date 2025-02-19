import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX
font1=cv2.FONT_HERSHEY_COMPLEX #opencv fonts

img=cv2.imread(r"media\polygons.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,threshold= cv2.threshold(gray,240,255,cv2.THRESH_BINARY)#min max ve y�ntem parametreleriyle threshold i�lemi yap�ld�
contours,_=cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#contourlara ula�t�k

for cnt in contours:#contourlara daha da yakla�ma i�lemi yap�ld�
    epsilon=0.01*cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt, epsilon, True)

    cv2.drawContours(img,[approx],0,(0),5)

    x=approx.ravel()[0]#approx ile ka� de�er oldu�unu tutuyor 
    y=approx.ravel()[1]

    if len(approx)==3:#approxun i�erdi�i de�ere g�re �ekillere isim verdik
        cv2.putText(img,"Triangle",(x,y),font,1,(0))

    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y),font,1,(0))

    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),font1,1,(0))

    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),font1,1,(0))

    else:
        cv2.putText(img,"Ellipse",(x,y),font,1,(0))

cv2.imshow("IMG",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



