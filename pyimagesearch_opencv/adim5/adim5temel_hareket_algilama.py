"""
-hareket algilama için arka plan çikarma önemlidir
Video akışımızın arka planı büyük ölçüde statiktir ve bir videonun ardışık kareleri üzerinde değişmez. 
Bu nedenle, arka planı modelleyebilirsek, önemli değişiklikler için onu izleriz.
Önemli bir değişiklik varsa, bunu tespit edebiliriz - bu değişiklik normalde videomuzdaki harekete karşılık gelir.


"""

# gerekli paketleri içeri aktardık
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
# eğer video yüklemezsek kamerayı kullanacaktır
if args.get("video", None) is None:
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
# argüman olarak kamera kullanılmadıysa videoyu kullanır
else:
	vs = cv2.VideoCapture(args["video"])
# video akışındaki ilk kareyi başlatır
#Video dosyamızın ilk karesi hareket içermeyecek ve yalnızca arka plan içerecektir 
# - bu nedenle, videonun yalnızca ilk karesini kullanarak video akışımızın arka planını modelleyebiliriz.
firstFrame = None
# frameler üzerinde bir döngü 
while True:
	# frameler okunur ve önceki frame ile karşılaştırır
	frame = vs.read()
	frame = frame if args.get("video", None) is None else frame[1]
	text = "bos"
	# çerçeve yakalanamadıysa o zaman video bitirilir
	if frame is None:
		break
	# frameler boyutlandırılır, gri tona çevirilir, blur ile bulanıklaştırılır(bu yumuşatma frameler arası küçük farklılıkların göz ardı edilmesi için gerekli)
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	# ilk kare yoksa il kare gri olarak tanımlanır
	if firstFrame is None:
		firstFrame = gray
		continue
	
    # mevcut kare ve önceki kare arasındaki mutlak farkı hespalayın
	frameDelta = cv2.absdiff(firstFrame, gray)
	#thereshold işlemi gerçekleştirin
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
	# delikleri kapatmak için dilate uyguladık ve konturları bulduk, sıraladık
	thresh = cv2.dilate(thresh, None, iterations=2)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# konturlar üzerinde döngü
	for c in cnts:
		# kontur çok küçükse görmezden gelin
		if cv2.contourArea(c) < args["min_area"]:
			continue
		# kontur için sınırlayıcı kutuyu hesaplayın, çerçeve çizin ve metni güncelleyin
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "dolu"
		
        # metni ve zamanı yazdırın
	cv2.putText(frame, "durum: {}".format(text), (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	# görüntüleyin
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	key = cv2.waitKey(1) & 0xFF
	# 'q' ya basınca görüntü durur
	if key == ord("q"):
		break
# kamerayı temizleyin ve açık pencereyi kapatın
vs.stop() if args.get("video", None) is None else vs.release()
cv2.destroyAllWindows()