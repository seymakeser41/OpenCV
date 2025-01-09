import cv2
#resmi aldık
img=cv2.imread("python_opencv_project/OpenCV/test_images/eye.png")
#cascade dosyalarını tanımladık
face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")
eye_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/eye.xml")
#gri tona çevirdik
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#yüz koordinatlarını tespit ettik
faces=face_cascade.detectMultiScale(gray,1.3,5)
#koordinatlara dikdörtgen çizerek yüzleri işaretledi
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
#bulduğumuz yüzü resimden kesip o resim üzerinden göz arayacak   
img2=img[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+w]
#gözlerin koordinatını tespit etti
eyes=eye_cascade.detectMultiScale(gray2)
#gözlerin bulunduğu yere dikdörtgen çizecek
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
