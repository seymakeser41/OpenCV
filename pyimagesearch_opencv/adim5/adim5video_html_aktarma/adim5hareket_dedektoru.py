# gerekli paketleri içeri aktar
import numpy as np
import imutils
import cv2

class SingleMotionDetector:
	def __init__(self, accumWeight=0.5):#akra planı hem ön hem arka olarak yüzde elli default değer tanımlar
		# birikmiş ağırlık faktörünü tutun
		self.accumWeight = accumWeight
		# akara plan modelini başlat
		#accumWeight (Ağırlık) daha büyük  ise, arka plan ne kadar az olursa  ağırlıklı ortalama toplanırken hesaba katılacaktır.
        # Tersine, daha küçük ise, arka plan ne kadar fazla olursa  ortalama hesaplanırken dikkate alınacaktır.
		self.bg = None
		
	def update(self, image):
		# akra plan modeli yok ise başlatın
		if self.bg is None:
			self.bg = image.copy().astype("float")
			return
		# birikmiş ağırlıklı ortalamayla arka plan modelini güncelleyin
		cv2.accumulateWeighted(image, self.bg, self.accumWeight)
		
	def detect(self, image, tVal=25):
		# Arka plan modeli arasındaki mutlak farkı hesaplayın ve görüntü geçti, ardından delta görüntüsünü eşikleyin
		delta = cv2.absdiff(self.bg.astype("uint8"), image)
		thresh = cv2.threshold(delta, tVal, 255, cv2.THRESH_BINARY)[1] #tVal: Belirli bir pikseli "hareket" olarak işaretlemek veya işaretlememek için kullanılan eşik değeri
		# erezyon ve genişlemeyle küçük gürültüleri azaltın
		thresh = cv2.erode(thresh, None, iterations=2)
		thresh = cv2.dilate(thresh, None, iterations=2)
		
        # eşikli görüntünün kopyası üzerinden konturları bulun ve hareket için minimum ve maksimum sınırlayıcı kutu bölgeleri başlatın
		cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		(minX, minY) = (np.inf, np.inf)
		(maxX, maxY) = (-np.inf, -np.inf)
		
        # kontur bulunmazsa None değer döndürür(hareket bulunamadı)
		if len(cnts) == 0:
			return None
		# aksi takdirde konturlar üzerinde döngü
		for c in cnts:
			# konturun sınırlayıcı kutusunu hesaplayın ve 
            # minimum ve maksimum sınırlayıcı kutu bölgelerini güncellemek için kullanın
			(x, y, w, h) = cv2.boundingRect(c)
			(minX, minY) = (min(minX, x), min(minY, y))
			(maxX, maxY) = (max(maxX, x + w), max(maxY, y + h))
		# aksi takdirde, sınırlayıcı kutu ile birlikte eşikli görüntüyü döndürün
		return (thresh, (minX, minY, maxX, maxY))