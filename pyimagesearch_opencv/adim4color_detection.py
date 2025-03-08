"""
OPENCV VE PYTHON RENK ALGILAMA 
-renkler için alt ve üst sinirlar belirlenir ve daha sonra aradığımız rengi dışarda bırakan bi maske uygulanır 
"""
#kütüphaneleri dahil ettik
import numpy as np
import imutils
import cv2
#argparse kullanarak resmi dahil etme işlemi
"""
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the image file")
args = vars(ap.parse_args())
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())
"""
#resmi dahil ettik
image = cv2.imread(r"C:\Users\seyma\Desktop\media\toybox.png") 
cv2.imshow("Image", image)
#sınırların bir listesini oluşturduk BGR'a göre
#ilk satırda, görüntümüzdeki R >= 100, B >= 15 ve G >= 17 olan ve R <= 200,
#  B <= 56 ve G <= 50 olan tüm piksellerin kırmızı olarak kabul ediyoruz hepsi bu mantıkla resimdeki kırmızı,mavi,sarı ve gri renklerin sınırıdır
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

# sınırlar üzerinde gezinerek işlem işlem yapıyoruz
for (lower, upper) in boundaries:
	# sınırları bir numpy dizisinde topluyoruz
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# belirlenen sınırlar içerisindeki renkleri bulup maske uyguluyoruz , bitwise and işlemi ile birlikte
	mask = cv2.inRange(image, lower, upper)
	output = cv2.bitwise_and(image, image, mask = mask)
	# görüntüyü göster
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)










cv2.waitKey(0)