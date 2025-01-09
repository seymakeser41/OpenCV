#cascade kullanmak araç tespitinde çok verimli değildir
import cv2
#cascade dosyasını tanımladı
car_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/car.xml")
#resmi dahil etti
img=cv2.imread("python_opencv_project/OpenCV/test_images/car.jpg")
#gri tona çevirdi
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cascade kullanarak arabaları tespit etti
cars=car_cascade.detectMultiScale(gray,1.1,1)
#bulunulan koordinatlara dikdörtgen çizerek işaretledi
for (x,y,w,h) in cars:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
#görüntüledi   
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
