import cv2
#webcamden videoyu dahil ettik
vid=cv2.VideoCapture(0)
#cascade dosyalarını dahil ettik
face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")
smile_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/smile.xml")
#whle döngüsüyle videodaki her frame aynı işlemleri yaptı
while 1:
    _,frame=vid.read()#frameleri çektik
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(480,360))#boyutlandırdık
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#boz tona çevirdi
    faces=face_cascade.detectMultiScale(gray,1.5,9)#yüzleri buldu
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)#bulduğu yüzü dikdörtgenlerle işaretledi

     #bulunan bölgeyi resimlerden ayırdık,gülümsemeleri bu alanda tarıcak
    roi_frame=frame[y:y+h,x:x+h]
    roi_gray=gray[y:y+h,x:x+h]
    #gülümsemeleri taradı
    smiles=smile_cascade.detectMultiScale(roi_gray)
    #bulduğu gülümsemeleri dikdörtgenlerle işaretledi
    for (sx,sy,sw,sh) in smiles:
        cv2.rectangle(roi_frame,(sx,sy),(sx+sw,sy+sh),(0,0,255),2)
    cv2.imshow("video",frame)  
    
    if cv2.waitKey(5) &  0xFF == ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()