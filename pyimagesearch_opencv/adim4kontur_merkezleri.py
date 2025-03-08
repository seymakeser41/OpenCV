"""
OPENCV KONTUR MERKEZLERİ:
-gri tonlama çevir
-yüksek frekanslı görüntüyü azaltmak için bulanıklaştırma(gaus yumuşatma)
-kenar algılama ve eşikleme kullanarak görüntüyü ikili hale getirme
-kontur algılamayı kullanarak beyaz bölgelerin konumunu bul   --->findCotours
-kontur bölgesi için görüntü momenti hesaplanır              --->cv2.moment 
-kontur merkezine odaklanılır , yazı yazılır 
"""

# gerekli paketleri içeri aktar
import argparse
import imutils
import cv2
# argüman ayrıştırıcıları oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the input image")
args = vars(ap.parse_args())
# resmi yükle 
image = cv2.imread(args["image"])
#gri moda çevir
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#blur ile bulanıklaştır
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#threshold uygula
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

#konturları bul ve sırala
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

#konturlar üzerinde bir döngü oluştur
for c in cnts:
	# konturların merkezini hesapla
	M = cv2.moments(c)
	#eğer sıfırsa atlar, diğer türlü sıfıra bölme hatası verir
	if M["m00"]==0:
		continue
	
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])
	# konturları çiz , merkezine çember koy ve yazı yaz
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(image, "center", (cX - 20, cY - 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	# resmi göster
	cv2.imshow("Image", image)
	cv2.waitKey(0)