# gerekli paketleri içeri aktardık
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
# argüman ayrıştırıcalarını oluşturun ve ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,help="max buffer size")
args = vars(ap.parse_args())

# HSV formatına göre nesne renginin alt ve üst değerlerini belirledik
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
#  izlenen noktaların listesini tutun, çerçeve sayacını naşlatın ve koordinat deltalarını 0 olarak ayarlayın
pts = deque(maxlen=args["buffer"])
counter = 0
(dX, dY) = (0, 0)
direction = ""
# bir video yolu verilmediyse web kamerasını kullanır
if not args.get("video", False):
	vs = VideoStream(src=0).start()
# eğer yüklendiyse video dosyasını kullanır
else:
	vs = cv2.VideoCapture(args["video"])
# kamera bekleme süresi
time.sleep(2.0)

#tüm frameler için işlem yap
while True:
	# frameleri oku
	frame = vs.read()
	# verilen videoyu veya web kamerasından görüntüyü işleyin
	frame = frame[1] if args.get("video", False) else frame
	# eğer bir frame yakalayamadıysak video bitmiştir
	if frame is None:
		break
	# frameleri boyutlandır, bulanıklaştır, hsv formatına döndür
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	# yeşil maskeyi uygula ,erozyon ve dilate işlemi ile maskeden kalan küçük eksikleri kapat
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	# maskedeki konturları bulun ve sıralayın 
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	
    # eğer kontur bulduysa yapılacak işlemler
	if len(cnts) > 0:
		# en büyük konturu bulur , konturu kapayan çemberi hesaplayın , ve bu kontur değeri ile merkezi bulun
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		# yarıçap minimum boyuttan büyükse yapılacak işlemler
		if radius > 10:
			# merkezi bulunan daireyi çizin ve noktaları güncelleyin
			cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
			pts.appendleft(center)
			
    # belirlenen noktalar arasında bir döngü
	for i in np.arange(1, len(pts)):
		# nokta yoksa yoksay 
		if pts[i - 1] is None or pts[i] is None:
			continue
		# yeterli nokta biriktirilip biriktirilmediğini kontrol edin
		if counter >= 10 and i == 1 and pts[-10] is not None:
			# x ve y arasındaki farkı hesaplayın , koordinat yönü için değişken başlatın
			dX = pts[-10][0] - pts[i][0]
			dY = pts[-10][1] - pts[i][1]
			(dirX, dirY) = ("", "")
			# x yönünde fark edilir hareket varsa doğuya
			if np.abs(dX) > 20:
				dirX = "doğu" if np.sign(dX) == 1 else "bati"
			# y yönün de fark edilir hareket olursa kuzey
			if np.abs(dY) > 20:
				dirY = "kuzey" if np.sign(dY) == 1 else "güney"
			# her iki yön de doluysa boş tutulur
			if dirX != "" and dirY != "":
				direction = "{}-{}".format(dirY, dirX)
			# yanlızca bir yön doluysa o yöne gider
			else:
				direction = dirX if dirX != "" else dirY
				
            # kalınlığı hesaplayın ve bağlantı çizgilerini çizin 
		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	# hareket açılarını ve yönünü yazdırın
	cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.65, (0, 0, 255), 3)
	cv2.putText(frame, "dx: {}, dy: {}".format(dX, dY),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0, 0, 255), 1)
	# frameleri göster
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	counter += 1
	# 'q' tuşuna basınca durdur
	if key == ord("q"):
		break
# video kullanmıyorsak kamera akışını durdurur
if not args.get("video", False):
	vs.stop()
# kamerayı serbest bırakın
else:
	vs.release()

cv2.destroyAllWindows()
				
            

