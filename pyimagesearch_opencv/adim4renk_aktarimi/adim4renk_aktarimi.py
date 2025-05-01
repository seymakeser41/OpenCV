"""
GÖRÜNTÜLER ARASINDA SÜPER HIZLI RENK AKTARIMI: 
renk aktarim algoritmasi ;
1. kaynak görüntü gir (taklit edilmesini istediğiniz renk uzayını içerir)   sourcetarget , color_transfer
2. L*a*b* renk alanına dönüştür resimleri
3. kanalları bölün 
4. her kanal için ortalama ve standart sapmasını hesapla       image_stats
5. görüntünün kanallarının ortalamasını kanallardan çıkarın
6. kanalları standart sapması oranıyla ölçeklendirin             source_target
7. kanalların ortalamasını ekleyin 
8. [0,255] aralık dışında değerleri kırpın
9. kanallari birleştirin 
10. L*a*b* dan RGB ye çevirin
"""
#BU KOD SAYFASI adim4renk_aktarimi_kod.py dosyasında kullanılacaktır
# gerekli paketleri içeri aktar
import numpy as np
import cv2
def color_transfer(source, target,clip=True, preserve_paper=True):
	# görüntüleri RGB'den L * ab * renk alanına dönüştürün,
	# kayan nokta veri türünü kullandığınızdan emin olun (not: OpenCV
	# float'ların 32 bit olmasını bekler, bu nedenle 64 bit yerine bunu kullanın)
	source = cv2.cvtColor(source, cv2.COLOR_BGR2LAB).astype("float32")
	target = cv2.cvtColor(target, cv2.COLOR_BGR2LAB).astype("float32")
	
    #  Kaynak ve hedef görüntüler için renk istatistiklerini hesaplayın
	(lMeanSrc, lStdSrc, aMeanSrc, aStdSrc, bMeanSrc, bStdSrc) = image_stats(source)
	(lMeanTar, lStdTar, aMeanTar, aStdTar, bMeanTar, bStdTar) = image_stats(target)
	# Ortalamayı hedef görüntüden çıkarın
	(l, a, b) = cv2.split(target)
	l -= lMeanTar
	a -= aMeanTar
	b -= bMeanTar
	# standart sapmalara göre ölçeklendirin
	l = (lStdTar / lStdSrc) * l
	a = (aStdTar / aStdSrc) * a
	b = (bStdTar / bStdSrc) * b
	# kaynak ortalamasını ekleyin
	l += lMeanSrc
	a += aMeanSrc
	b += bMeanSrc
	# Piksel yoğunluklarını dışarıda kalırlarsa [0, 255] olarak kırpın
	l = np.clip(l, 0, 255)
	a = np.clip(a, 0, 255)
	b = np.clip(b, 0, 255)
	#  kanalları birleştirin ve RGB rengine geri dönüştürün
	# 8 bitlik işaretsiz tamsayı verilerini kullandığınızdan emin olun
	transfer = cv2.merge([l, a, b])
	transfer = cv2.cvtColor(transfer.astype("uint8"), cv2.COLOR_LAB2BGR)
	
	# aktarılan renkli görüntüyü döndür
	return transfer

def image_stats(image):
	# Her kanalın ortalama ve standart sapmasını hesaplayın
	(l, a, b) = cv2.split(image)
	(lMean, lStd) = (l.mean(), l.std())
	(aMean, aStd) = (a.mean(), a.std())
	(bMean, bStd) = (b.mean(), b.std())
	# renk istatistiklerini döndür
	return (lMean, lStd, aMean, aStd, bMean, bStd)