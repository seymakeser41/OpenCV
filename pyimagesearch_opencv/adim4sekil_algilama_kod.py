# gerekli paketler içe aktarılır
from adim4sekil_algilama import ShapeDetector
import argparse
import imutils
import cv2
# argüman ayrıştırıcısını oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())

# resmi yükle, boyutlandır(daha küçük çünkü daha iyi tahmin edilir)
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
# gri tona çevir, bulanıklaştır, threshold uygula
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# konturları bulun, sıralayın ve şekil dedektörünü çalıştırın
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()

# konturlarda gezinin
for c in cnts:
	# merkezi bulun, konturun adını tespit edin
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	shape = sd.detect(c)
	# kontur (x, y) koordinatlarını yeniden boyutlandırma oranıyla çarpın,
	# Daha sonra konturları ve şeklin adını resmin üzerine çizin	c = c.astype("float")
	c = (c.astype("float") * ratio).astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 2)
	# sonucu görüntüleyin
	cv2.imshow("Image", image)
	cv2.waitKey(0)