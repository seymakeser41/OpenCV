
import cv2

def nothing(x):
    pass

img1=cv2.imread("python_opencv_project/media/aircraft.jpg")
img2=cv2.imread("python_opencv_project/media/balls.jpg")

img1=cv2.resize(img1,(640,480))#resimleri birbirine dönüştürmek için aynı boyutta olmaları gerek
img2=cv2.resize(img2,(640,480))

output=cv2.addWeighted(img1,0.5,img2,0.5,0)#iki resmi ağırlıklarıyla beraber birleştirdik
windowName="transition program"
cv2.namedWindow(windowName)#penceremizi isimlendirdik

cv2.createTrackbar("alpha-beta",windowName, 0,1000,nothing)#tracbarı oluşturduk

while 1:
    cv2.imshow(windowName,output)
    alpha=cv2.getTrackbarPos("alpha-beta",windowName)/1000#trackbardan aldığımız değeri alphaya verdik
    beta=1-alpha
    output=cv2.addWeighted(img1,alpha,img2,beta,0)#trackbardaki değerlere göre resimleri birleştirdik
    print(alpha,beta)
    
    if cv2.waitKey(1)==27:
        break
    
cv2.destroyAllWindows()