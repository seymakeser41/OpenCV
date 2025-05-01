"""
Adim #1: Bilgisayarla görme tekniklerini kullanarak renkli bir topun varlığını tespit edin.
# 2 Adim: Video karelerinde hareket ederken topu takip edin ve hareket ettikçe önceki konumlarını çizin.
"""

# gerekli paketler içeri aktarıldı
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
# argüman ayrıştırıcı oluşturuldu ve ayırıştırdı
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,help="max buffer size")
args = vars(ap.parse_args())

# yeşil renk bir topta uygulanacağı için alt ve üst sınırlar beliritilir
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
#izlenen noktalarının bir listesini oluşturun
pts = deque(maxlen=args["buffer"])
# eğer video yüklendiyse video yüklenmediyse kamera kullanılır
if not args.get("video", False):
	vs = VideoStream(src=0).start()

else:
	vs = cv2.VideoCapture(args["video"])
# kameranın veya videonun bekleme süresidir
time.sleep(2.0)
#frameler için sonsuz döngü
while True:
	# frameler okunur
	frame = vs.read()
	# videodan frameyi işleyin
	frame = frame[1] if args.get("video", False) else frame
	#bir frame bulamazsak video biter
	if frame is None:
		break
	# boyutlandırdık, bulanıklaştırdık, gri tona çevirdik
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# yeşil bir maske uygulayın ve küçük boşluklar için erezyon ve dilate işlemi uygulayın
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	
    # maskedeki konturları bulun (topun merkezi koordinatları) ve ilk merkezi none tanımlayın
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	# kontur bulunursa devam edin
	if len(cnts) > 0:
		# maskedeki en büyük konturu bulun (minimum çevreleyen daireyi hesaplamak için) ve merkezi hesaplayın
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# yarıçap minimum boyuttan büyükse devam edin
		if radius > 10:
			# daireyi çizin (merkezine ve etrafına) ve noktaları güncelleyin
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
	# update the points queue
	pts.appendleft(center)
	
     #izlenen noktalar üzerinde döngü
	for i in range(1, len(pts)):
		# nokta yoksa yoksay ve devam et 
		if pts[i - 1] is None or pts[i] is None:
			continue
		# çizgi kalınlıklarını hesaplayın ve bağlantı çizgilerini çizin
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	# frameleri görüntüleyin
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# 'q' ya basınca çıkın
	if key == ord("q"):
		break
# bir video kullanmıyorsak kamera akışını durdurur
if not args.get("video", False):
	vs.stop()
# kamerayı serbest bırak
else:
	vs.release()

cv2.destroyAllWindows()