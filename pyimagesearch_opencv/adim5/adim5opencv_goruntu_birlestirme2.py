# gerekli paketleri içeri aktar
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
# arguman ayrıştırıcı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,help="path to the output image")
ap.add_argument("-c", "--crop", type=int, default=0,help="whether to crop out largest rectangular region")
args = vars(ap.parse_args())
# Giriş resimlerine giden yolları alın ve resim listemizi başlatın
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []
# görüntü yolları üzerinde döngü yapın, her birini yükleyin ve bunları resimler dizisine ekleyin
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)
# OpenCV'nin görüntü birleştirici nesnesini başlatın ve ardından birleşik görüntüyü oluşturun
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

# durum '0' ise, OpenCV görüntü başarıyla gerçekleştirildi
if status == 0:
	# En büyük dikdörtgeni kırpmamız gerekip gerekmediğini kontrol edin
	if args["crop"] > 0:
		#  Dikişli görüntüyü çevreleyen 10 piksellik bir kenarlık oluşturun
		print("[INFO] cropping...")
		stitched = cv2.copyMakeBorder(stitched, 10, 10, 10, 10,cv2.BORDER_CONSTANT, (0, 0, 0))
		# Dikişli görüntüyü gri tonlamaya dönüştürün ve eşikleyin
		# Öyle ki sıfırdan büyük tüm pikseller 255 olarak ayarlanır
		# (ön plan), diğerleri ise 0 (arka plan) olarak kalır
		gray = cv2.cvtColor(stitched, cv2.COLOR_BGR2GRAY)
		thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]
		
        # Eşik görüntüsündeki tüm dış konturları bulun ve ardından en büyük konturu bulun
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		c = max(cnts, key=cv2.contourArea)
		# Dikişli görüntü bölgesinin dikdörtgen sınırlayıcı kutuyu içerecek olan maske için bellek ayırın.
		mask = np.zeros(thresh.shape, dtype="uint8")
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)
		
        # maskenin iki kopyasını oluşturun: biri gerçek minimum dikdörtgen bölgemiz olarak, 
        # diğeri de minimum dikdörtgen bölgeyi oluşturmak için kaç pikselin kaldırılması gerektiğine dair bir sayaç olarak kullanılmak üzere
		minRect = mask.copy()
		sub = mask.copy()
		# çıkarılan görüntüde sıfır olmayan piksel kalmayana kadar döngüye devam edin
		while cv2.countNonZero(sub) > 0:
			# minimum dikdörtgen maskeyi aşındırın ve ardından eşiklenmiş görüntüyü minimum dikdörtgen maskeden çıkarın, 
            # böylece sıfır olmayan piksel kalıp kalmadığını sayabiliriz
			minRect = cv2.erode(minRect, None)
			sub = cv2.subtract(minRect, thresh)
			
        # minimum dikdörtgen maskede konturları bulun ve ardından sınırlayıcı kutu (x, y)-koordinatlarını çıkarır
		cnts = cv2.findContours(minRect.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		c = max(cnts, key=cv2.contourArea)
		(x, y, w, h) = cv2.boundingRect(c)
		# sınırlayıcı kutu koordinatlarını kullanarak nihai dikilmiş görüntü
		stitched = stitched[y:y + h, x:x + w]
		
        # Çıktı dikişli görüntüyü diske yazın
	cv2.imwrite(args["output"], stitched)
	# Çıktı dikişli görüntüyü ekranımızda görüntüleyin
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
# aksi takdirde, muhtemelen yeterli anahtar nokta olmaması nedeniyle dikiş başarısız oldu)
else:
	print("[INFO] image stitching failed ({})".format(status))