from turtledemo.penrose import start

import cv2
import numpy as np

img=cv2.imread(r"media/star.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,127,255,0)
contours,_=cv2.findContours(thresh, 2,1)

cnt=contours[0]
hull=cv2.convexHull(cnt,returnPoints = False)#dış bükey örtü için gereken değerleri tuttuk
defects=cv2.convexityDefects(cnt,hull)#kusurları arıyoruz
d=defects.shape[0]
for i in range(d): #defektsin boyutu kadar dönücek
    s,e,f,d=defects[i,0] #star point , end point, fardes point(en uzak nokta)(içteki noktalar),distance (mesafe)
    star=tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,star,end,[0,255,0],2) # noktalara çizgi çizdik
    cv2.circle(img,far,5,[0,255,0],-1) # dışbükey yerlere daire çizdik

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


