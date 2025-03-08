#NONETYPE HATALARINI ÇÖZME
#-ya çalışacak belgeyi bulamaz ya da çalışıp doğru değer döndürmez
import cv2
image = cv2.imread("hdsjdhsjdhk")#yanlış bir adres verdiğimiz için nonetype hatası verir 
(h, w, d) = image.shape #çalışacak görüntüyü bulamaz ve bu satırda hata verir
print("w: {}, h: {}, d: {}".format(w, h, d))

cv2.imshow("Image", image)
cv2.waitKey(0)