import cv2

img=cv2.imread(r"python_opencv_project/OpenCV/test_images/face.png")

face_cascade=cv2.CascadeClassifier("python_opencv_project/OpenCV/haarCascade/frontalface.xml")
#cascade dosyasını tanımlamak için bu fonksiyon kullanılır

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#gri tonlara çevirdik

faces=face_cascade.detectMultiScale(gray,1.3,7)
#cascadeyi kullanarak yüzleri bulucak, koordinatları tutacak
#ilk değişken nesne aradığımız resim, ikinci ölçeklendirme değeri, üçüncü bir bölgede o kadar aranan nesneden bulsun ki eminlik sağlasın(bu değer artarsa daha hatasız bulur)
#4 değer döndürür, ilk ikisi sol üst koordinat, 3. yükseklik ve diğeri genişlik

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,0,255),2)#bulunan koordinatlara dikdörtgen çizerek belirttik

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

