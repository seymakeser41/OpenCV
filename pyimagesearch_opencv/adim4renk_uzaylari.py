#cv2.cvtColor kullanarak değişen renk uzaylarının etkisini anlamak ve görselleştirmek için kullanışlıdır.
"""
aydınlatma koşullarıyla çalışırken elde etmeye çalışmanız gereken üç hedef:
1-High contrast:Görüntünüzdeki İlgi Alanları arasındaki kontrastı en üst düzeye çıkarmaya çalışmalısınız
2-Generalizable:Aydınlatma koşullarınız, bir nesneden diğerine iyi çalışacak kadar tutarlı olmalıdır.
3-Stable:Kararlı, tutarlı ve tekrarlanabilir aydınlatma koşullarına sahip olmak

OpenCV'de dört renk alanı/modeli:
1-RGB
2-HSV (Otova)
3-L*a*b*
4-Gri tonlamalı

aydınlatma, bilgisayarla görme algoritmanızın başarısı ve başarısızlığı arasındaki fark anlamına gelebilir.





"""

# kütüphaneleri import ettik
import argparse
import cv2
# argparse kullanarak resmi dahii ettik
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("RGB", image)

#tek tek kanalların her birini döngü ile görüntüleyin
for (name, chan) in zip(("B", "G", "R"), cv2.split(image)):
	cv2.imshow(name, chan)
	
#hsv renk formatına çevirdi
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
# tek tek kanallarda dolaşıp görüntüledik
for (name, chan) in zip(("H", "S", "V"), cv2.split(hsv)):
	cv2.imshow(name, chan)
	
#görüntüyü L * a * b * renk alanına dönüştürün ve gösterin
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)
# görüntüyü L * a * b * renk alanına dönüştürün ve gösterin
for (name, chan) in zip(("L*", "a*", "b*"), cv2.split(lab)):
	cv2.imshow(name, chan)

#gri formata dönüştürdük ve görüntüledik 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

	



cv2.waitKey(0)
cv2.destroyAllWindows()