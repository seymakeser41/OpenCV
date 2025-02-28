#temel opencv işlemleri
import imutils   #imutils paketini import ettik
import cv2

image = cv2.imread(r"C:\Users\seyma\Desktop\media\jurrasicpark.jpg") #görüntüyü yükledik
(h, w, d) = image.shape #görüntü boyutlarını hesapladık 
print("width={}, height={}, depth={}".format(w, h, d))# boyutları yazdırdık

(B, G, R) = image[100, 50] #resmin x=100 y=50 noktasındaki pikselin renk değerlerini tutar
print("R={}, G={}, B={}".format(R, G, B)) #değerleri yazdırdık
cv2.imshow("Image", image)

roi = image[60:160, 320:420] #seçtiğimiz koordinat değerleri arasındaki bölgeyi kırpar
cv2.imshow("ROI", roi)

resized = cv2.resize(image, (200, 200)) #resmi istediğimiz boyutlarda görüntüledik
cv2.imshow("Fixed Resizing", resized)

r = 300.0 / w #resmin en boy oranını koruyarak boyutlandırma yaptık
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)

resized = imutils.resize(image, width=300) #bu oranlı boyutlandırma işlemini imutils paketini kullanarak kolayca yapabiliriz
cv2.imshow("Imutils Resize", resized)

center = (w // 2, h // 2) #resmin merkezini bulduk
M = cv2.getRotationMatrix2D(center, -45, 1.0) #rotasyon matrisi hesaplanıyor
rotated = cv2.warpAffine(image, M, (w, h))  #y ekseni etrafında matrisi kullanarak döndürüyor
cv2.imshow("OpenCV Rotation", rotated)

rotated = imutils.rotate(image, -45) #döndürme işlemini imutils paketi kullanarak kolayca yapabiliriz
cv2.imshow("Imutils Rotation", rotated)

rotated = imutils.rotate_bound(image, 45) #döndürme işlemindeki kayıpları bu komutla düzeltiriz resim tam gözükür
cv2.imshow("Imutils Bound Rotation", rotated)

blurred = cv2.GaussianBlur(image, (11, 11), 0) #blur işlemi ile bulanıklaştırırız matris ne kadar büyük olursa o kadar bulanıklaşır
cv2.imshow("Blurred", blurred)

output = image.copy() #resmin kopyasını kullanmak için bir değişkene atarız
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2) #dikdörtgen çizeriz
cv2.imshow("Rectangle", output)

output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1) #belirtilen koordinata bir daire çizer 
cv2.imshow("Circle", output)

output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)#çizgi çizer
cv2.imshow("Line", output)

output = image.copy()
cv2.putText(output, "OpenCV + Jurassic Park", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2) #belirtilen noktaya belirtilen fontta yazı yazar
cv2.imshow("Text", output)

cv2.waitKey(0)