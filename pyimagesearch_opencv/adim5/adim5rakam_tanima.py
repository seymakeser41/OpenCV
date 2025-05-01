"""
7 segmentli ekran kullanılır , 128 olası durum içerir ve bunlardan 10 tanesi rakamlardır 

Adım #1: LCD'yi termostat üzerinde konumlandırın. Bu, plastik kabuk ile LCD arasında yeterli kontrast olduğu için kenar algılama kullanılarak yapılabilir.
Adım #2: LCD'yi çıkarın. Bir giriş kenarı haritası verildiğinde, konturları bulabilir ve dikdörtgen şekilli ana hatları arayabilirim - en büyük dikdörtgen bölge LCD'ye karşılık gelmelidir.
 Bir perspektif dönüşümü bana LCD'nin güzel bir şekilde çıkarılmasını sağlayacaktır.
Adım #3: Rakam bölgelerini çıkarın. LCD'nin kendisine sahip olduğumda, rakamları çıkarmaya odaklanabilirim. Rakam bölgeleri ile LCD'nin arka planı arasında kontrast var gibi göründüğü için, eşikleme ve morfolojik işlemlerin bunu başarabileceğinden eminim.
Adım #4: Rakamları tanımlayın. OpenCV ile gerçek rakamları tanımak, rakam ROI'sini yedi segmente bölmeyi içerecektir. Oradan, belirli bir segmentin "açık" mı yoksa "kapalı" mı olduğunu belirlemek için eşikli görüntüye piksel sayımı uygulayabilirim.

"""

# gerekli paketler içeri aktarılır
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
# Tanımlayabilmemiz için rakam segmentleri sözlüğünü tanımlayın
DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 1, 0): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9
}

# resmi yükle
image = cv2.imread(r"C:\Users\seyma\Desktop\media\termostat.png")
# ön işleme için yeniden boyutlandır, gri tona çevir , bulanıklaştır ve kenarları bul
image = imutils.resize(image, height=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 50, 200, 255)
# konturları bul, sırala 
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
displayCnt = None
# konturlar üzerinde döngü 
for c in cnts:
	# konturu yaklaşık olarak belirle
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
	# konturun 4 köşesi varsa ekranı bulduk sayarız
	if len(approx) == 4:
		displayCnt = approx
		break
	
#Termostat ekranını çıkarın, bir perspektif dönüşümü uygulayın
warped = four_point_transform(gray, displayCnt.reshape(4, 2))
output = four_point_transform(image, displayCnt.reshape(4, 2))

# threshold uygulayın ve görüntüyü eşikleyin, Eşikli görüntüyü temizleme işlemleri uygulayın
thresh = cv2.threshold(warped, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# eşiklenmiş görüntü üzerinden konturları bulun, bulunan konturlar için kontur listesi oluşturun
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
digitCnts = []
# rakam alanları adayları arasında döngü 
for c in cnts:
	# konturun sınırlayıcı kutusunu hesaplayın
	(x, y, w, h) = cv2.boundingRect(c)
	# eğer kontur yeterince büyükse bir rakam olmalı, listeye ekle
	if w >= 15 and (h >= 30 and h <= 40):
		digitCnts.append(c)
# Konturları soldan sağa sıralayın, gerçek rakamlar bir liste başlatın
digitCnts = contours.sort_contours(digitCnts,method="left-to-right")[0]
digits = []

# rakamların her biri üzerinde döngü
for c in digitCnts:
	# ROI rakamını çıkarın
	(x, y, w, h) = cv2.boundingRect(c)
	roi = thresh[y:y + h, x:x + w]
	# 7 segmentin her birinin genişliğini ve yüksekliğini hesaplayın
	(roiH, roiW) = roi.shape
	(dW, dH) = (int(roiW * 0.25), int(roiH * 0.15))
	dHC = int(roiH * 0.05)
	# 7 segmentten oluşan seti tanımlayın
	segments = [
		((0, 0), (w, dH)),	# üst
		((0, 0), (dW, h // 2)),	# sol üst
		((w - dW, 0), (w, h // 2)),	# sağ üst
		((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # merkez
		((0, h // 2), (dW, h)),	# sol alt
		((w - dW, h // 2), (w, h)),	# sağ alt
		((0, h - dH), (w, h))	# alt
	]
	on = [0] * len(segments)
	
    # segmentler üzerinde döngü
	for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
		# segment ROI'sini çıkarın, segmentte eşikli piksellerin toplam sayısını sayın, 
		# segmentin alanını hesaplayın
		segROI = roi[yA:yB, xA:xB]
		total = cv2.countNonZero(segROI)
		area = (xB - xA) * (yB - yA)
		# Sıfır olmayan piksellerin alanı % 50'den büyükse   segmenti "açık" olarak işaretleyin
		if total / float(area) > 0.5:
			on[i]= 1
	# rakamı arayın ve resmin üzerine yazın
	digit = DIGITS_LOOKUP[tuple(on)]
	digits.append(digit)
	cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
	cv2.putText(output, str(digit), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)
	
# rakamları göster
print(u"{}{}.{} \u00b0C".format(*digits))
cv2.imshow("Input", image)
cv2.imshow("Output", output)
cv2.waitKey(0)