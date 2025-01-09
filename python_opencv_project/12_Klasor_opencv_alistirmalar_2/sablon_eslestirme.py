import cv2
import numpy as np

img_path="python_opencv_project/media/starwars.jpg"
template_path="python_opencv_project/media/starwars2.jpg"
img=cv2.imread(img_path)
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template=cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)#resmi alıp direk gray formatta okuyabiliriz
w,h=template.shape[::-1]
result=cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)#eşleştiren iki resmi bu fonksiyonla yaparız
#resultdaki en beyaz nokta template resminin sol üstüdür

location=np.where(result>=0.9)#sonuç 1 e ne kadar yakınsa o kordinatları bulur

for point in zip(*location[::-1]):#where fonksiyonundan alınan dizi zip ile anlamlı hale gelir , tersten alarak dikdörtgen çizilebilcek hale getirir
    cv2.rectangle(img,point,(point[0]+w, point[1]+h),(0,255,0),3)    #bulunan noktaya dikdörtgen çizgi template kadar böylece bulmuş oldu

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()