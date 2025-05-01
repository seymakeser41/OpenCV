# gerekli paketler içeri aktarıldı
from adim5barkod import detection
from imutils.video import VideoStream
import argparse
import time
import cv2
# argüman ayrıştırıcılar oluşturulur ve ayrıştırılır.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",help="path to the (optional) video file")
args = vars(ap.parse_args())
# Video yolu sağlanmadıysa, kamerayı referans alın.
if not args.get("video", False):
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
# aksi takdirde videoyu yükleyin
else:
	vs = cv2.VideoCapture(args["video"])
# frameler üzerinde bir döngü oluşturun
while True:
	# 'VideoCapture' veya 'VideoStream' nesnesinden geçerli çerçeveyi alın
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
 
	# videonun sonuna ulaşıp ulaşmadığımızı kontrol edin.
	if frame is None:
		break
	# Görüntüdeki barkodu tespit edin
	box = detection(frame)
	# Bir barkod bulunursa, çerçeveye bir sınırlayıcı kutu çizin
	if box is not None:
		cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
	# Çerçeveyi gösterin ve kullanıcı bir tuşa basarsa kaydedin
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# eğer 'q' tuşuna basılırsa döngüyü durdurun
	if key == ord("q"):
		break
# Bir video dosyası kullanmıyorsak, video dosyası akışını durdurun
if not args.get("video", False):
	vs.stop()
# aksi takdirde, kamerayı serbest bırakın
else:
	vs.release()
cv2.destroyAllWindows()