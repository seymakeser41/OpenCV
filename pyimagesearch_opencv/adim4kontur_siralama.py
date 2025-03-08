"""
PYTHON VE OPENCV KULLANARAK KONTURLARI SIRALAMA:
-Boyutlara/alanlara göre sırala      ---->sort_contours(contourlar , yöntem)
-sağdan sola , aşağıdan yukarı (azalan tersi için artan) gibi tek bir işleve göre sırala
"""

# gerekli paketler içe aktarılır
import numpy as np
import argparse
import imutils
import cv2
def sort_contours(cnts, method="left-to-right"):
	# dizini soldan sağa olarak sıralamaya başlayın
	reverse = False
	i = 0
	# ters sıralamanız gerekiyorsa
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
	# sınırlayıcı kutunun x koordinatı yerine y koordinatına göre sıralama yapıyorsak
	if method == "top-to-bottom" or method == "bottom-to-top":i = 1
	# sınırlayıcı kutuların listesini oluşturun ve bunları yukarı doğru sıralayın
	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),key=lambda b:b[1][i], reverse=reverse))
	# sıralanmış kontur ve sınırlayıcı kutu listesini döndürün
	return (cnts, boundingBoxes)

def draw_contour(image, c, i):
	#kontur merkezini hesaplayın
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# kontur numarasını yazdırın
	cv2.putText(image, "#{}".format(i + 1), (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX,1.0, (255, 255, 255), 2)
	# resmi döndürün
	return image


# argüman ayrıştırıcılarını oluşturun ve ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
ap.add_argument("-m", "--method", required=True, help="Sorting method")
args = vars(ap.parse_args())
# resimleri yükleyin ve birikmiş kenar görüntüsünü başlatın
image = cv2.imread(args["image"])
accumEdged = np.zeros(image.shape[:2], dtype="uint8")
# sırasıyla mavi,yeşil ve kırmızı kanallar üzerinde gezin
for chan in cv2.split(image):
	# kanalı bulanıklaştırın, kenarlarını çıkarın, birleştirin 
	chan = cv2.medianBlur(chan, 11)
	edged = cv2.Canny(chan, 50, 200)
	accumEdged = cv2.bitwise_or(accumEdged, edged)
# sonucu göster
cv2.imshow("Edge Map", accumEdged)

# konturlar bulunur, sıralanır, alanlarına göre ilk 5 alınır
cnts = cv2.findContours(accumEdged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]
orig = image.copy()
# sıralanmış, seçilmiş konturlarda gezilir ve konturlar çizilir
for (i, c) in enumerate(cnts):
	orig = draw_contour(orig, c, i)
# ilk resim görüntülenir
cv2.imshow("Unsorted", orig)
# methoda göre sıralama gerçekleşir
(cnts, boundingBoxes) = sort_contours(cnts, method=args["method"])
# sıralanmış konturlar çizilir
for (i, c) in enumerate(cnts):
	draw_contour(image, c, i)
# sıralanmış resim görüntülenir
cv2.imshow("Sorted", image)
cv2.waitKey(0)