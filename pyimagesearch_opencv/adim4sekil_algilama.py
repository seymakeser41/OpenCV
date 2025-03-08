"""
OPENCV ŞEKİL ALGILAMA :
kontur yaklaşımı bir eğrinin bir çizgiye yaklaşımı varsayımına dayanır
kontur çevresi hesaplanır ve orijinal kontur çevresinin %1-5i arası yaklaşık alınır 
köşe sayısına göre şekil tahmin edilir
"""
#bu kod sayfası adim4sekil_algilama_kod.py dosyasında kullanılmıştır

# gerekli paketler içe aktarılır
import cv2


class ShapeDetector:
	def __init__(self):
		pass
	def detect(self, c):
		# şekil adını başlatın ve konturu yaklaşık olarak belirleyin
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)
		
        # eğer 3 köşe varsa üçgen
		if len(approx) == 3:
			shape = "triangle"
		# 4köşe varsa kare mi dikdörtgen mi diye bakılır
		elif len(approx) == 4:
			#konturun sınırlayıcı kutusu hesaplanıp en boy oranı hesaplanır
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
			# eğer oran 1e yakınsa kare değilse dikdörtgen olarak belirlenir
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
		# 5 köşeli beşgen
		elif len(approx) == 5:
			shape = "pentagon"
		# daha fazla köşe kullanıyorsa çember olarak tanımlar
		else:
			shape = "circle"
		# şeklin adını döndürür
		return shape

