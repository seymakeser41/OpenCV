#gerekli pakatler import edildi
import numpy as np
import imutils
import cv2
#argparse kullanarak resmi dahil etmek
"""
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the image file")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
"""
#görüntüyü dahil ettik
image=cv2.imread(r"C:\Users\seyma\Desktop\media\hap.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #gri tona çevirdik
gray = cv2.GaussianBlur(gray, (3, 3), 0) #blur ile bulanıklaştırdık
edged = cv2.Canny(gray, 20, 100) #kenarları bulduk
#konturları bulduk
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts) # konturları sıraladık
#bulduğumuz konturların üzerinde işlem yapacağız 
if len(cnts) > 0:
	# en büyük kontur alanını buluyor ve çizer
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	# kontur alanının bölgesini, koordinatlarını kullanarak ayırdı ve maske uyguladı
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,mask=maskROI)
    #döndürme işlemi gerçekleşir
for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate(imageROI, angle)
		cv2.imshow("Rotated (Problematic)", rotated)
		cv2.waitKey(200)
	# kayıpları önemseyerek döndürme gerçekleşir
for angle in np.arange(0, 360, 15):
		rotated = imutils.rotate_bound(imageROI, angle)
		cv2.imshow("Rotated (Correct)", rotated)
		cv2.waitKey(200)
