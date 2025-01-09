import cv2

vid=cv2.VideoCapture("python_opencv_project/OpenCV/test_videos/faces.mp4")

face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")#cascade tanımladı

while 1:
    _,frame=vid.read()#frameleri okudu
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#gri tona çevirdik
    
    faces=face_cascade.detectMultiScale(gray,1.1, 2)#yüzleri aradı koordinatları buldu
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)#koordinatları kullanarak dikdörtgen çizdi
    cv2.imshow("image",frame)
    
    if cv2.waitKey(5) & 0xFF== ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()