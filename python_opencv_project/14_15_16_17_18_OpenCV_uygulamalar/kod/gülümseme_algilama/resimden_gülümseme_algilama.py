import cv2
#resmi aldık
img=cv2.imread("python_opencv_project/OpenCV/test_images/smile.jpg")
#cascade dosyalarını tanımladık
face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")
smile_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/smile.xml")
#gri tona çevirdik
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#yüz koordinatlarını tespit ettik
faces=face_cascade.detectMultiScale(gray,1.3,5)
#koordinatlara dikdörtgen çizerek yüzleri işaretledi
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
#bulduğumuz yüzü resimden kesip o resim üzerinden gülümseme arayacak   
roi_img=img[y:y+h,x:x+w]
roi_gray=gray[y:y+h,x:x+w]
#gülümseme koordinatını tespit etti
smiles=smile_cascade.detectMultiScale(roi_gray)
#gülümsemelerin bulunduğu yere dikdörtgen çizecek
for (sx,sy,sw,sh) in smiles:
    cv2.rectangle(roi_img,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)
cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()