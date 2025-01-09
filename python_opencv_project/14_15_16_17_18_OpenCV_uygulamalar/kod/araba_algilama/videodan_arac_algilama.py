#cascade kullanmak araç tespitinde çok verimli değildir
import cv2
#cascade dosyasını tanımladı
car_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/car.xml")
#videoyu dahil etti
vid=cv2.VideoCapture("python_opencv_project/OpenCV/test_videos/car.mp4")
#işlemleri tüm framler için while döngüsünde yaptı
while 1:
    #frame çekti
    _,frame=vid.read()
    #boyutlandırdı
    frame=cv2.resize(frame,(600,480))
    #gri tona çevirdi
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cascade ile arabaları aradı
    cars=car_cascade.detectMultiScale(gray,1.1,2)
    #bulunan araba koordinatlarına dkdörtgen çizerek işaretledi
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #görüntüledi   
    cv2.imshow("frame",frame)
    #görüntüyü kapatma şartları belirtildi
    if cv2.waitKey(5) & 0xFF== ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()