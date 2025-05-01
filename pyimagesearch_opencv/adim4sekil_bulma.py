#-siyah şekilleri algılama ve beyaza çevirme 

# gerekli paketleri yükle
import numpy as np
import argparse
import imutils
import cv2
# argüman ayrıştırıcı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
args = vars(ap.parse_args())
# resmi yükle
image = cv2.imread(args["image"])

#resimdeki tüm siyah şekilleri bulmak için aralık belirle ve bu aralıktaki nesneleri bul
lower = np.array([0, 0, 0])
upper = np.array([15, 15, 15])
shapeMask = cv2.inRange(image, lower, upper)

# conturları bul ve sırala , kaç siyah şekil olduğunu konturları tutan değişkenin uzunluğu ile yazdır 
cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
print(" {} siyah şekil buldu".format(len(cnts)))
cv2.imshow("Mask", shapeMask)
# konturlarda bir döngü oluştur
for c in cnts:
	# konturları çiz
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.imshow("Image", image)
	cv2.waitKey(0)