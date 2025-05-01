# gerekli paketleri içeri aktar
import numpy as np
import argparse
import imutils
import cv2
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "path to the image file")
args = vars(ap.parse_args())
# resmi yükle ve gri tona çevir
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# OpenCV 2.4 kullanarak hem x hem de y yönünde görüntülerin Scharr gradyan büyüklüğü temsilini hesaplayın
ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)
# Y gradyanını x gradyanından çıkarın
#Bu çıkarma işlemini gerçekleştirerek, görüntünün yüksek yatay gradyanlara ve düşük dikey gradyanlara sahip bölgeleriyle baş başa kalırız.
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
#görüntüyü bulanıklaştırın ve eşikleyin
blurred = cv2.blur(gradient, (9, 9))
(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
#Bir kapanış kernel oluşturun ve bunu eşikli görüntüye uygulayın
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))#barkodun dikey şeritleri arasındaki boşlukları kapatmamızı sağlar.
closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #morfolojik işlemimizi gerçekleştiriyoruz ve böylece çubuklar arasındaki boşlukları kapatmaya çalışıyoruz.
# erezyon ve genişlemeyle küçük gürültülerden kurtulur
closed = cv2.erode(closed, None, iterations = 4)
closed = cv2.dilate(closed, None, iterations = 4)
# Eşikli görüntüdeki konturları bulun, ardından konturları büyüğe göre sıralayın, en büyüğü tutun
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
#En büyük konturun döndürülmüş sınırlayıcı kutusunu hesaplayın
rect = cv2.minAreaRect(c)
box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
box = box.astype(np.int32)
# Algılanan barkodun etrafına bir sınırlayıcı kutu çizin ve resmi görütüleyin
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)