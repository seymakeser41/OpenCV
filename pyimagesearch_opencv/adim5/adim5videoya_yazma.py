# gerekli paketler içe aktarılır
from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
# argüman ayrıştırıcılar oluşturulur ve ayrıştırılır
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,help="path to output video file")# Çıkış video dosyasının yolu (zorunlu)
ap.add_argument("-p", "--picamera", type=int, default=-1,help="whether or not the Raspberry Pi camera should be used") #PiCamera kullanılsın mı (1: evet, -1: hayır)
ap.add_argument("-f", "--fps", type=int, default=20,help="FPS of output video")
ap.add_argument("-c", "--codec", type=str, default="MJPG",help="codec of output video")
args = vars(ap.parse_args())

# video akışını başlatın ve kameraya izin verin
print("[INFO] warming up camera...")
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
time.sleep(2.0)
# Fourcc'yi alın ve yazıcıyı,boyutları, sıfır dizisini none olarak başlatın
#medya dosyalarında kullanılan bir video codec bileşeni, sıkıştırma formatı, renk veya piksel formatı için bir tanımlayıcı olan "dört karakter kodu"nun kısaltmasıdır
fourcc = cv2.VideoWriter_fourcc(*args["codec"])
writer = None
(h, w) = (None, None)
zeros = None #RGB ayrımı için kullanılır


# videodaki frameler üzerinde sonsuz döngü
while True:
	# frameleri oku ve yeniden boyutlandır(300 )
	frame = vs.read()
	frame = imutils.resize(frame, width=300)
	# yazıcı kontrol edilir
	if writer is None:
		# frame gelince boyutlar belirlenir, video yazıcı oluşturulur(4 farklı görüntü yan yana yerleştirilecek)
		(h, w) = frame.shape[:2]
		writer = cv2.VideoWriter(args["output"], fourcc, args["fps"],(w * 2, h * 2), True)
		zeros = np.zeros((h, w), dtype="uint8")
		
        # BGR olarak frameler ayrılır ve her kanal kendi rengiyle tekrar birleştirilir
	(B, G, R) = cv2.split(frame)
	R = cv2.merge([zeros, zeros, R])
	G = cv2.merge([zeros, G, zeros])
	B = cv2.merge([B, zeros, zeros])
	# 4 görüntü birleştrilir, orjinal görüntü sol üstte ve R,G,B görüntüleri sırasıyla sağ üst, sağ alt ve sol alttadır
	output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
	output[0:h, 0:w] = frame
	output[0:h, w:w * 2] = R
	output[h:h * 2, w:w * 2] = G
	output[h:h * 2, 0:w] = B
	# görüntü kaydedilir ve gösterilir
	writer.write(output) #çıktı frame'ini dosyaya yazar.
	
    # frameleri göster
	cv2.imshow("Frame", frame)
	cv2.imshow("Output", output)
	key = cv2.waitKey(1) & 0xFF
	# eğer `q` tuşuna basılırsa çıkış
	if key == ord("q"):
		break
# temizlik yapılır
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
vs.stop()
writer.release()
		
        