import cv2
#videoyu dahil ettik
vid=cv2.VideoCapture("python_opencv_project/OpenCV/test_videos/eye.mp4")
#cascade dosyalarını dahil ettik
face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/eye.xml")
#whle döngüsüyle videodaki her frame aynı işlemleri yaptı
while 1:
    _,frame=vid.read()#frameleri çektik
    frame=cv2.resize(frame,(480,360))#boyutlandırdık
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#boz tona çevirdi
    faces=face_cascade.detectMultiScale(gray,1.3,5)#yüzleri buldu
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)#bulduğu yüzü dikdörtgenlerle işaretledi

     #bulunan bölgeyi resimlerden ayırdık,gözleri bu alanda tarıcak
    roi_frame=frame[y:y+h,x:x+h]
    roi_gray=gray[y:y+h,x:x+h]
    #gözleri taradı
    eyes=eye_cascade.detectMultiScale(roi_gray)
    #bulduğu gözleri dikdörtgenlerle işaretledi
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow("video",frame)  
    
    if cv2.waitKey(5) &  0xFF == ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()
    
    
