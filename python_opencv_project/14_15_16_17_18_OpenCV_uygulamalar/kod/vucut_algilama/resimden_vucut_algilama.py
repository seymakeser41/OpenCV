import cv2
#resmi dahil etti 
img=cv2.imread("python_opencv_project/OpenCV/test_images/body.jpg")
#cascade dosyasını dahil etti
body_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/fullbody.xml")
#gri tona çevirdi
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cascade ile vücutları taradı
bodies=body_cascade.detectMultiScale(gray,1.1,2)
#vücut koordinatlarını dikdörtgen çizerek işaretledi
for (x,y,w,h) in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
    