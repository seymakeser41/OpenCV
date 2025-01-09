import cv2
import numpy as np

def nothing(x):
    pass

img=np.zeros((512,512,3),np.uint8) #tuval oluşturduk
cv2.namedWindow("image") #pencereye trackbar ile aynı pencerede görünmesi için isin verdik

cv2.createTrackbar("R","image",0,255,nothing) #adı , penceresi,başlangıç ve bitiş değerleri,ve çalışması için boş bir fonk girilerek trackbar oluşturuldu
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
switch="0:OFF, 1ON"
cv2.createTrackbar(switch,"image",0,1,nothing)

while True:     #tüm değiştirdiğim değerleri alabimesi için sonsuz bir döngü kurduk ve çıkış değeri belirledik
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

    r=cv2.getTrackbarPos("R","image") #trackbar değerlerini aldık
    g = cv2.getTrackbarPos("G", "image")
    b=cv2.getTrackbarPos("B","image")
    s = cv2.getTrackbarPos(switch, "image")

    if s==0: #switch değerine göre değişim yapabileceğiz
        img[:]=[0,0,0]

    if s==1:
       img[:]=[b,g,r] #tüm img değerlerine bgr değerlerini atadık

cv2.destroyAllWindows()
cv2.waitKey(0)
