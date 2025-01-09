import cv2
import numpy as np

img=cv2.imread(r"C:\Users\ŞEYMA KESER\PycharmProjects\python_opencv_project\media\text.png")
img1=cv2.imread(r"C:\Users\ŞEYMA KESER\PycharmProjects\python_opencv_project\media\contour.pngcontour.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)#fonksiyonun resimde değişiklik yapması için tipini değiştitmememiz gerek
corners=cv2.goodFeaturesToTrack(gray,8000,0.1,10)#köşeleri yapacak fonksiyona resmi,maks köşe sayısısnı,kaliteyi,iki köşe arası uzaklığı girerek çalıştırdık
corners=np.int8(corners)#köşeleri çizebilmek için tipi değiştirmemiz gerek

for corner in corners:
    x,y=corner.ravel()#aldığımız değerler ikili bu yüzden tek değer için tek satır yaptık
    cv2.circle(img,(x,y),3,(0,0,255),-1)

gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)#fonksiyonun resimde değişiklik yapması için tipini değiştitmememiz gerek
corners1=cv2.goodFeaturesToTrack(gray,1000,0.8,5)#köşeleri yapacak fonksiyona resmi,maks köşe sayısısnı,kaliteyi,iki köşe arası uzaklığı girerek çalıştırdık
corners1=np.int8(corners1)

for corner in corners1:
    x,y=corner.ravel()#aldığımız değerler ikili bu yüzden tek değer için tek satır yaptık
    cv2.circle(img,(x,y),3,(0,0,255),-1)
cv2.imshow("corner",img)
cv2.imshow("corner1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

