# gerekli paketleri içeri aktar
import numpy as np
import cv2
import imutils
def detection(image):
	# görüntüyü gri tonlamaya çevir
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#OpenCV 2.4 kullanarak hem x hem de y yönünde görüntülerin scharr gradyan(kenar değişimleri) büyüklüğü temsilini hesaplayın
	ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
	gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)#Sobel fonksiyonu, kenar belirleme filtresidir.
	gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
	# Y gradyanını x gradyanından çıkarın. Bu, özellikle barkod gibi belirgin çizgileri vurgular.
	gradient = cv2.subtract(gradX, gradY)
	gradient = cv2.convertScaleAbs(gradient)#convertScaleAbs: Piksel değerlerini mutlak değere çevirir ve 8-bit forma dönüştürür (görüntü için gerekli).
	# resmi bulanıklaştır ve threshol uygulayarak eşikle
	blurred = cv2.blur(gradient, (9, 9))
	(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
	# Dikdörtgen kernel ile kapanma işlemi (closing) uygulanır.
    # Kapanma işlemi, siyah boşlukları kapatır, bu da barkod gibi bağlantılı bölgelerin düzgün çıkmasını sağlar.
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
	closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
	# gürültüleri azaltmak için erezyon ve tekrar nesneleri büyütmek için genişletme işlemi uygulanır
	closed = cv2.erode(closed, None, iterations=4)
	closed = cv2.dilate(closed, None, iterations=4)
	# eşiklenen görüntü üzerinde konturlar bulunur
	#RETR_EXTERNAL: Sadece dış konturları alır.
    # CHAIN_APPROX_SIMPLE: Gereksiz noktaları atar, daha az veri ile çalışır.
    # imutils.grab_contours: OpenCV versiyonuna göre konturları almayı kolaylaştırır.
	cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	# Eğer hiç kontur yoksa, fonksiyon None döndürerek barkod bulunmadığını belirtir.
	if len(cnts) == 0:
		return None
	# Konturlar alanına göre sıralanır, en büyük olan (muhtemelen barkod) seçilir.
	c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
	rect = cv2.minAreaRect(c)#cv2.minAreaRect: Kontur için en küçük döndürülmüş dikdörtgeni bulur.
	box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)#BoxPoints: Döndürülmüş dikdörtgenin dört köşesini verir.
	box = box.astype(np.int32)
	# Bu dört köşe koordinatları geri döndürülür. Barkodun bulunduğu alan budur.
	return box