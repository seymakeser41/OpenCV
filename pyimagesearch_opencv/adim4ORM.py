"""
ORM, PYTHON VE OPENCV KULLANARAK KABARCIK SAYFASI ÇOKTAM SEÇMELİ TARAYICI VE TEST DERECELENDİRİCİ:
Optik İşaret Tanıma(ORM): insan tarafından işaretlenmiş bilgileri otomatik olarak analiz etme ve sonuçlarını yorumlama süreci
1. sınavı bir görüntüde tespit edin
2. kuş bakışı görünüm için perspektif dönüşümü uygulayın
3. baloncuk kümesini olası yanıt seçeneklerini çıkarın
4. soruları satır halinde sıralayın
5. her satır için doğru baloncuğu belirle
6. seçimlerde doğru cevabı arayın
"""
# gerekli paketler içeri aktarıldı
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
# argüman ayrıştırıcı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())
# kaçıncı şıkların doğru olduğunu belirterek cevap anahtarı oluşturun
ANSWER_KEY = {0: 1, 1: 4, 2: 0, 3: 3, 4: 1}

#resmi yükle , gri moda çevir, bulanıklaştır ve kenarları bul 
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 75, 200)

# konturları bul, sırala
cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
docCnt = None
# kontur bulunduysa bu işlemleri gerçekleştirir
if len(cnts) > 0:
	# konturları boyutlarına göre sıraladı
	cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
	# konturlar üzerinde bir döngü
	for c in cnts:
		# konturu yaklaşık olarak belirleyin
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.02 * peri, True)
		#konturun 4 noktası varsa kağıdı bulduk sayabiliriz
		if len(approx) == 4:
			docCnt = approx
			break
		
    
# gri tondaki ve normal görüntyü kuş bakışı görünüm için perspektif dönüşümü yapın
paper = four_point_transform(image, docCnt.reshape(4, 2))
warped = four_point_transform(gray, docCnt.reshape(4, 2))

# threshold uygulayın(akra plan siyah ön plan beyaz şekilde cevaplı kağıdı oluşturun)
thresh = cv2.threshold(warped, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# eşikli görüntüde konturları bulun, sorulara karşılık gelen kontur listesini oluşturun
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
questionCnts = []
# konturlar üzerinde döngü
for c in cnts:
	# konturu sınırlayıcı kutuyu bulun ve en boy oranını hesaplayın
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)
	# konturu bir soru olarak işaretlemek için en boy oranı yaklaşık 1 olan geniş alanı bulur, soru listesine ekler
	if w >= 20 and h >= 20 and ar >= 0.9 and ar <= 1.1:
		questionCnts.append(c)
		
# soru konturlarını sıralayın ve doğru eşleşme sayısı için bir dğer tutun
questionCnts = contours.sort_contours(questionCnts,method="top-to-bottom")[0]
correct = 0
# her sorunun 5 olası cevabı olduğu için 5li gruplar halinde incelenir
for (q, i) in enumerate(np.arange(0, len(questionCnts), 5)):
	# mevcut soru için konturları sıralar 
	cnts = contours.sort_contours(questionCnts[i:i + 5])[0]
	bubbled = None
	
# sıralanmış konturlar üzerinde döngü
	for (j, c) in enumerate(cnts):
		# sadece şıkları öne çıkararak konturları çizeriz
		mask = np.zeros(thresh.shape, dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		# maskeyli bitwise işlemi ile uygulayıp 0 olmayan piksellerin sayısını sayar
		mask = cv2.bitwise_and(thresh, thresh, mask=mask)
		total = cv2.countNonZero(mask)
		# sıfrı olmayan pikseller toplamı mevcut toplamdan daha büyükse cevabı inceliyoruz
		if bubbled is None or total > bubbled[0]:
			bubbled = (total, j)
			
    # doğru cevbın kontur rengi belirtilir
	color = (0, 0, 255)
	k = ANSWER_KEY[q]
	# kabarcıklı cevabın doğru olup olmadığı kontrol edilir
	if k == bubbled[1]:
		color = (0, 255, 0)
		correct += 1
	# doğru olan cevabın ana hatları çizilir
	cv2.drawContours(paper, [cnts[k]], -1, color, 3)

#sıanava giren kişinin belgesi yüklenir ve sonuçları verilir
score = (correct / 5.0) * 100
print("[INFO] score: {:.2f}%".format(score))
cv2.putText(paper, "{:.2f}%".format(score), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
cv2.imshow("Original", image)
cv2.imshow("Exam", paper)
cv2.waitKey(0)