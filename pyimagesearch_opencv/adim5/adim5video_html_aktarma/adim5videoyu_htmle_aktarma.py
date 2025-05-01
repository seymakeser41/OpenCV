"""
Flask ve OpenCV kullanarak videoyu bir web tarayicisina aktarmak
Flask, Python programlama dilinde yazilmiş popüler bir mikro web çerçevesidir.
--pip install flask ile yükleyin
Arka plan çikarma ve hareket algilama gerçekleştirmek için farkli siniflar kullanilacak
adim5hareket_dedektoru.py kullanildi
"""
#temel hareket dedektörü uygulama
"""
Hareket dedektörü algoritmamiz, hareketi arka plan çikarma biçimine göre algilayacaktir.

Çoğu arka plan çikarma algoritmasi şu şekilde çalişir:

Önceki N karenin ağirlikli ortalamasini biriktirme
Geçerli kareyi alma ve bunu karelerin ağirlikli ortalamasindan çikarma
Piksel değerlerinde önemli farkliiklar olan bölgeleri vurgulamak için çikarma çiktisinin eşiklenmesi (ön plan için "beyaz" ve arka plan için "siyah")
Gürültüyü gidermek için erozyon ve genişleme gibi temel görüntü işleme tekniklerinin uygulanmasi
Hareket içeren bölgeleri çikarmak için kontur algilamayi kullanma
"""
# gerekli paketler içeri aktarıldı
from adim5hareket_dedektoru import SingleMotionDetector
from imutils.video import VideoStream #Raspberry Pi için
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import datetime
import imutils
import time
import cv2

# Çıkış çerçevesini ve iş parçacığı güvenliğini sağlamak için kullanılan bir kilidi başlatın
# çıktı çerçevelerinin değiş tokuşu (birden fazla tarayıcı/sekme olduğunda kullanışlıdır)
outputFrame = None
lock = threading.Lock()
# bir flask nesnesi başlat
app = Flask(__name__)
# Video akışını başlatın ve kamera sensörünün ısınmasına izin verin
#vs = VideoStream(usePiCamera=1).start() #pi camerası için
vs = VideoStream(src=0).start()
time.sleep(2.0)

@app.route("/")
def index():  #görevi html sayfamızda Flaskı çağırmaktır
	# oluşturulan şablonu döndür
	return render_template("index.html")

def detect_motion(frameCount):#frameCount (çerçeve sayısı), arka planımızı oluşturmak için gereken minimum kare sayısıdır
	#video akışına, çıktı karesine küresel referanslar alın ve değişkenleri kilitle
	global vs, outputFrame, lock #vs (nesne), çıktı çerçevesi, kilit 
	# Hareket dedektörünü ve toplam kare sayısını başlatın
	
	md = SingleMotionDetector(accumWeight=0.1) #Ağırlıklı ortalama hesaplanırken değer daha yüksek ağırlıklandırılacaktır.
	total = 0 # arka plan modelimizi oluşturmak için yeterli sayıda karenin okunduğundan emin olmamız gerekecek.
    # video akişindaki frameler üzerinde döngü
	while True:
		# video akışından bir sonraki kareyi okuyun, yeniden boyutlandırın
		# Çerçeveyi gri tonlamaya dönüştürün ve bulanıklaştırın
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)
		# Geçerli zaman damgasını alın ve çerçeveye yazın
		timestamp = datetime.datetime.now()
		cv2.putText(frame, timestamp.strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		# Toplam çerçeve sayısı makul bir arka plan modeli oluşturmak için yeterli sayıya ulaştıysa çerçeveyi işlemeye devam edin
		if total > frameCount:
			# görüntüdeki hareketi algıla
			motion = md.detect(gray)
			# çerçevede hareket bulunup bulunmadığını kontrol edin
			if motion is not None:
				# diziyi çıkarın ve çıkış karesindeki hareket alanını sınırlayan bölgeyi çizin
				(thresh, (minX, minY, maxX, maxY)) = motion
				cv2.rectangle(frame, (minX, minY), (maxX, maxY),(0, 0, 255), 2)
		
		# Arka plan modelini güncelleyin ve şu ana kadar okunan kare sayısını arttırın
		md.update(gray)
		total += 1
		# Kilidi alın, çıkış çerçevesini ayarlayın ve kilidi bırakın
		with lock:
			outputFrame = frame.copy()

def generate():
	# Çıktı çerçevesine genel referansları alın ve değişkenleri kilitleyin
	global outputFrame, lock
	# çıktı görüntüleri üzerinde gezinin
	while True:
		# Kilit alınana kadar bekleyin
		with lock:
			# Çıkış çerçevesinin mevcut olup olmadığını kontrol edin aksi takdirde döngüyü yineleyin
			if outputFrame is None:
				continue
			# çerçeveyi JPEG formatında kodlayın
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			# Çerçevenin başarıyla kodlandığından emin olun
			if not flag:
				continue
		# çıktı çerçevesini bayt biçiminde verir
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

#  Bunun yürütmenin ana iş parçacığı olup olmadığını kontrol edin
if __name__ == '__main__':
	# argüman ayrıştırıcıyı oluştur ve ayrıştır
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,help="# of frames used to construct the background model")
	args = vars(ap.parse_args())
	# Hareket algılama gerçekleştirecek bir iş parçacığı başlatın
	t = threading.Thread(target=detect_motion, args=(args["frame_count"],))
	t.daemon = True
	t.start()
	# Flask uygulamasını başlatın
	app.run(host=args["ip"], port=args["port"], debug=True,threaded=True, use_reloader=False)
# video durdur.
vs.stop()