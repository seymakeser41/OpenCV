"""
5 DKDA KICK-ASS MOBİL BELGE TARAYICI NASIL OLUŞTURULUR:
1. kenarları tespit et
2. görüntüyü temsil eden konturu bulmak için kenarları kullanın 
3. yukardan aşağıya görünümü bulmak için perspektif dönüşümü yapın
"""
# gerekli paketler içeri aktarıldı 
from adim4perspektif_dönüsümü import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image to be scanned")
args = vars(ap.parse_args())

#KÖŞE BELİRLEME

# resmi yükle ve boyutlandır
image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)
# gri tona çevir, bulanıklaştır,kenarları çiz
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
#resimleri görüntüle
print("STEP 1: Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#KONTURLARI BUL 
# konturları bul, alanlarına göre sırala
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
# konturlar üzerinde döngü
for c in cnts:
	# konturu yaklaşık olarak beirleyin
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# eğer yaklaşık konturun 4 noktası varsa ekranı bulduk sayabiliriz
	if len(approx) == 4:
		screenCnt = approx
		break
# çıktıları görüntüle
print("STEP 2: Find contours of paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#PERSPEKTİF DÖNÜŞÜMÜ

#orjinal resmi kuş bakışı görünüm için 4 nokta dönüşümü uyguladı
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
# çarpık görüntüyü gri tona çevitr ve siyah beyaz kağıt efekti vermek için threshold ile eşikleyin 
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255
# sonuçları görüntüle
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)