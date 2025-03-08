"""
OPENCV İLE KONTURLARDAKİ UÇ NOKTALARI BULMA :
-nesneyi ayırmak için eşikleme kullanılır 
-tespit edilen nesnenin dışbükey çerçevesi çizilip uç noktalar bulunup 
bu uç noktalara göre kontur merkezi ile orta bölge bulunur
"""

# gerekli paketler içe aktar
import imutils
import cv2
# resmi yükle, gri moda çevir, blur ile bulanıklaştır
image = cv2.imread(r"C:\Users\seyma\Desktop\media\hand.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
# threshold ve erozyon dan geçirip küçük gürültülü bölgeleri gidermek için temizleyin(dilate)
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
#konturları bulun, sıralayın ve en büyüğünü alın
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

# kontur boyunca en uç noktaları bulun
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

# nesnelerin ana hatlarını çizin 
# en sol kırmızı, en sağ yeşil,en üst mavi, en alt deniz mavisi olacak şekilde dairelerle bu noktaları belirtin
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 8, (0, 0, 255), -1)
cv2.circle(image, extRight, 8, (0, 255, 0), -1)
cv2.circle(image, extTop, 8, (255, 0, 0), -1)
cv2.circle(image, extBot, 8, (255, 255, 0), -1)
# resmi gösterin
cv2.imshow("Image", image)
cv2.waitKey(0)