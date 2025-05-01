# gerekli paketleri içeri aktar
from imutils.video import VideoStream
import imutils
import time
import cv2
# hareket belirginliği nesnesini ve videoyu başlatın
saliency = None
vs = VideoStream(src=0).start()
time.sleep(2.0)

# videonun her karesi için döngü
while True:
	# Dizili video akışından kareyi alın ve işlemi hızlandırmak için (500px) yeniden boyutlandırın
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	# belirginlik nesnemiz Yok ise, onu somutlaştırmamız gerekir
	if saliency is None:
		saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
		saliency.setImagesize(frame.shape[1], frame.shape[0])
		saliency.init()
		
    # Giriş çerçevesini gri tonlamaya dönüştürün ve belirginliği hesaplayın
	# Hareket modeline dayalı haritayı renklendirin
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	(success, saliencyMap) = saliency.computeSaliency(gray)
	saliencyMap = (saliencyMap * 255).astype("uint8")
	# çıktıyı görüntüle
	cv2.imshow("Frame", frame)
	cv2.imshow("Map", saliencyMap)
	key = cv2.waitKey(1) & 0xFF
 
	# 'q' tuşuna basılmışsa, döngüden çıkın
	if key == ord("q"):
		break
# videoyu serbest bırak
cv2.destroyAllWindows()
vs.stop()