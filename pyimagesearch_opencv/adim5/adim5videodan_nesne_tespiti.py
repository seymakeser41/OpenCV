#p logosunu tespit eder ama video yolu verilmeli çünkü usb kamera olmadığından bağlanamıyor

# gerekli paketler içeri aktarıldı
import argparse
import imutils
import cv2
# argüman ayrıştırıcı oluştruldu ve ayrıştırıldı
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
args = vars(ap.parse_args())
# video yüklenmediyse kamerayı kullanır
camera = cv2.VideoCapture(args["video"])


# sonsuz döngü 
while True:
	# geçerli çerçeveyi alın ve durum metnini başlatın
	(grabbed, frame) = camera.read()
	status = "hedef yok"
	# videonun sonuna ulaşıp ulaşmadığını kontrol edin 
	if not grabbed:
		break
	# çerçeveyi gri tona çevirin, bulanıklaştırın ve kenarları çizin
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (7, 7), 0)
	edged = cv2.Canny(blurred, 50, 150)
	# kenar haritalarında konturları bulun
	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	
    # konturlar üzerinde döngü
	for c in cnts:
		# konturlara yaklaşın 
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.01 * peri, True)
		# yaklaşılan konturun kabaca dikdörtgen olduğundan emin olun
		if len(approx) >= 4 and len(approx) <= 6:
			# yaklaşık konturun sınırlayıcı kutusunu hesaplayın ve
			# en boy oranını hesaplamak için sınırlayıcı kutuyu kullanın
			(x, y, w, h) = cv2.boundingRect(approx)
			aspectRatio = w / float(h)
			# orjinal konturun sağlamlığını hesaplayın 
			area = cv2.contourArea(c)
			hullArea = cv2.contourArea(cv2.convexHull(c))
			solidity = area / float(hullArea) #sağlamlık = orijinal alan / dışbükey gövde alanı
			# genişlik ve yüksekliğin, sağlamlığın ve konturun en boy oranına uygun sınırlar içindedir 
			keepDims = w > 25 and h > 25
			keepSolidity = solidity > 0.9
			keepAspectRatio = aspectRatio >= 0.8 and aspectRatio <= 1.2 #yaklaşık olarak kare
			# konturun tüm testlerimizi geçtiğinden emin olun
			if keepDims and keepSolidity and keepAspectRatio:
				# Hedefin etrafına bir taslak çizin ve durum metnini güncelleyin
				cv2.drawContours(frame, [approx], -1, (0, 0, 255), 4)
				status = "hedef(ler) alindi"
				# konturun merkezini hesaplayın ve hedefe artı işareti çizin 
				M = cv2.moments(approx)
				(cX, cY) = (int(M["m10"] // M["m00"]), int(M["m01"] // M["m00"]))
				(startX, endX) = (int(cX - (w * 0.15)), int(cX + (w * 0.15)))
				(startY, endY) = (int(cY - (h * 0.15)), int(cY + (h * 0.15)))
				cv2.line(frame, (startX, cY), (endX, cY), (0, 0, 255), 3)
				cv2.line(frame, (cX, startY), (cX, endY), (0, 0, 255), 3)
				
    # durum metnini yazın
	cv2.putText(frame, status, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0, 0, 255), 2)
	# frameleri gösterin
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# eğer 'q' basılırsa durun 
	if key == ord("q"):
		break
# kamerayı temizleyin, açık pencereyi kapatın
camera.release()
cv2.destroyAllWindows()