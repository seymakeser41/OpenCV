
# gerekli paketler içe aktarıldı
from adim4sekil_algilama import ShapeDetector
from adim4nesne_rengi_belirleme import ColorLabeler
import argparse
import imutils
import cv2
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())
#resmi yükle ve boyutlandır
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
# bulanıklaştır, gri tona çevir, lab renk tonuna çevir, threshold uyguladı
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
lab = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)
thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)[1]
# konturları bul ve sırala
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# nesne belirlemeyi ve renk belirlemeyi uygula
sd = ShapeDetector()
cl = ColorLabeler()

# konturlar üzerinde bir döngü
for c in cnts:
	# konturların merkezini hesaplayın
	M = cv2.moments(c)
	cX = int((M["m10"] / M["m00"]) * ratio)
	cY = int((M["m01"] / M["m00"]) * ratio)
	# konturların şeklini ve rengini belirle
	shape = sd.detect(c)
	color = cl.label(lab, c)
	# kontur (x, y) koordinatlarını yeniden boyutlandırma oranıyla çarpın,
	# Daha sonra konturların rengi ve şeklin adını çizin ve etiketleyin(yazdırın)
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	text = "{} {}".format(color, shape)
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.putText(image, text, (cX, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	# sonucu görüntüleyin
	cv2.imshow("Image", image)
	cv2.waitKey(0)