import cv2
#videoyu dahil ettik
vid=cv2.VideoCapture("python_opencv_project/OpenCV/test_videos/body.mp4")
#cascade dosyasını tanımladık
body_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/fullbody.xml")
#döngüyle tüm frameleri işlicez
while 1:
    _,frame=vid.read()#frameleri okudu
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#Gri tona çevirdi
    #vücütları taradık
    bodies=body_cascade.detectMultiScale(gray,1.2,2)
    #vücutları dikdörtgenlerle işretledik, videoya uygun dikey dörtgen için uzunlukları değiştirdik
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(y+h,x+w),(0,0,255),3)
    #görüntüledi
    cv2.imshow("video",frame)
    
    if cv2.waitKey(20) & 0xFF== ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()
    
    