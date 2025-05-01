"""

En yaygin sahne siniri türü "karartma"dir.
Bir videodan çizgi roman panellerini çıkarmanın püf noktası, hareketin ne zaman durduğunu tespit etmektir.

Bu görevi gerçekleştirmek için tek ihtiyacımız olan temel bir sahne sınırı algılama algoritmasıdır.
"""
# gerekli paketleri içeri aktar 
import argparse
import imutils
import cv2
import os
# argüman ayrıştırıcılari oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, type=str,help="path to input video file")#giriş videosu
ap.add_argument("-o", "--output", required=True, type=str,help="path to output directory to store frames")#çıktı dizini
ap.add_argument("-p", "--min-percent", type=float, default=1.0,help="lower boundary of percentage of motion")# Çerçeve hareketi yüzdesinin varsayılan alt sınırı.
ap.add_argument("-m", "--max-percent", type=float, default=10.0,help="upper boundary of percentage of motion")# Çerçeve hareketi yüzdesinin varsayılan üst sınırı.
ap.add_argument("-w", "--warmup", type=int, default=200,help="# of frames to use to build a reasonable background model")#Arka plan modelimizi oluşturmak için varsayılan kare sayısı
args = vars(ap.parse_args())

# arka plan çıkarıcısını başlat
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
# Belirli bir çerçevenin olup olmadığını temsil etmek için kullanılan bir boolean'ı başlatın
# yakalanan ve işlenen kare sayısını tutmak için sayaç başlatın
captured = False
total = 0
frames = 0
# video dosyasında genişlik ve yükseklikle işaretçiyi başlatın
vs = cv2.VideoCapture(args["video"])
(W, H) = (None, None)

# video kareleri üzerinde döngü
while True:
	# videodan bir kare alın
	(grabbed, frame) = vs.read()
	# bir çerçeve yoksa videonun sonuna ulaştık
	if frame is None:
		break
	# otjinal çerçeveyi kopyalayın daha sonra kaydedebiliriz
	#kareleri boyutlandırın ve maske uygulayın
	orig = frame.copy()
	frame = imutils.resize(frame, width=600)
	mask = fgbg.apply(frame)
	# Gürültüyü ortadan kaldırmak için bir dizi erozyon ve genişleme uygulayın
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	# Genişlik ve yükseklik boşsa, uzamsal boyutları alın
	if W is None or H is None:
		(H, W) = mask.shape[:2]
	# "Ön Plan" olan maskenin yüzdesini hesaplayın
	p = (cv2.countNonZero(mask) / float(W * H)) * 100
	
    # ön plan olarak çerçevenin hareket yüzdesi alt sınırdan az ise durgun bu nedenle çerçeve direk karemiz
	if p < args["min_percent"] and not captured and frames > args["warmup"]:
		# yakalanan çerçeveyi göster ve yakalanan durumunu güncelleyin
		cv2.imshow("Captured", frame)
		captured = True
		# çıktı çerçevesine giden yolu oluşturun ve toplam çerçeve sayısını arttırın
		filename = "{}.png".format(total)
		path = os.path.sep.join([args["output"], filename])
		total += 1
		# * Orijinal, yüksek çözünürlüklü * çerçeveyi diske kaydedin
		print("[INFO] saving {}".format(path))
		cv2.imwrite(path, orig)
	# aksi takdirde ya sahne değişiyor ya da ısınma aşamasında , arka plan modelini oluşturmak için sahne oturana kadar bekleriz
	elif captured and p >= args["max_percent"]:
		captured = False
		
    # çerçeveyi görüntüleyin ve bir tuşa basıp basılmadığını tespit edin
	cv2.imshow("Frame", frame)
	cv2.imshow("Mask", mask)
	key = cv2.waitKey(1) & 0xFF
	# "q" tuşuna basılmışsa, döngüden çıkın
	if key == ord("q"):
		break
	# çerçeve sayacını artırın
	frames += 1
# videoyu serbest bırak
vs.release()