import cv2
import numpy as np

img=cv2.imread(r"media/map.jpg")

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))#yumuşadı
ret,thresh=cv2.threshold(blur,40,255, cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE ) #contoursları bulduk
hull=[] #convex hull değerleri için boş bir dizi tanımladık

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i], returnPoints=False)) #false yazdığımız için indeksi döndürcek

bg=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8) #convex hullarla çizeceğimiz şekil için siyah ekran oluşturduk
for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(255,0,0),3,8) #contoursları çizdik 8 kesintisiz çizgi demek
    cv2.drawContours(bg, hull, i, (0,255, 0), 1, 8)# hulların contourslarını çizdik

cv2.imshow("image",bg)


cv2.waitKey(0)
cv2.destroyAllWindows()