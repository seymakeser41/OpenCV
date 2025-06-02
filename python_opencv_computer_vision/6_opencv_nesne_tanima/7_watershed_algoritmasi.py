import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü oku ve yedekle
img = cv2.imread(r"C:\Users\seyma\Desktop\media\coin_tespit.png")
img_copy = img.copy()
img_copy1 = img.copy()

# Görüntüyü griye çevir
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Gürültüyü azaltmak için median blur uygula
blur = cv2.medianBlur(img, 25)

# Blurlanmış görseli griye çevir
gray_blur = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)

# Eşikleme işlemi - coin'ler beyaz olsun diye ters threshold kullanılıyor
ret, th = cv2.threshold(gray_blur, 160, 255, cv2.THRESH_BINARY_INV)

# Alan tabanlı dış konturları tespit et
contours, hierarchy = cv2.findContours(th.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(img_copy, contours, i, (0, 0, 255), 10)

# Morfolojik açma işlemi - küçük gürültüleri temizlemek için
kernel = np.ones((3, 3), np.uint8)
morph = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=2)

# Dilation - foreground'ı büyütme
dt = cv2.dilate(morph, kernel, iterations=3)

# Distance transform işlemi - merkeze uzaklığı belirleme
dist_trans = cv2.distanceTransform(dt, cv2.DIST_L2, 5)

# Merkezlere odaklanmak için yeniden threshold
ret, th2 = cv2.threshold(dist_trans, 0.7 * dist_trans.max(), 255, 0)
th2 = np.uint8(th2)

# `unknown` bölgeyi tanımla: arka plan - ön plan
unknown = cv2.subtract(dt, th2)

# Sınırlayıcı etiketleme (connected components)
ret, markers = cv2.connectedComponents(th2)

# Etiket numaraları 0'dan başladığı için karışmasın diye 1 eklenir (arka plan 1 olacak)
markers = markers + 1

# Bilinmeyen alanları sıfırla
markers[unknown == 255] = 0

# Watershed işlemi (coin'leri ayırma)
waters = cv2.watershed(img, markers)

# Watershed çıktısı sınırları -1 olarak verir, onları işaretlemek için (isteğe bağlı)
img[waters == -1] = [0, 255, 0]

# Konturları çizmek için uygun tipte görüntü oluştur (binary hale getir)
# 1'den büyük olanlar foreground’dır
marker_mask = np.uint8(markers > 1) * 255

# Konturları bul ve çiz
contours1, hierarchy1 = cv2.findContours(marker_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours1)):
    if hierarchy1[0][i][3] == -1:
        cv2.drawContours(img_copy1, contours1, i, (0, 0, 255), 10)

# Görüntüleri göster
cv2.imshow('resim', img)
cv2.imshow('gri', gray)
cv2.imshow('blur', blur)
cv2.imshow('gri_blur', gray_blur)
cv2.imshow('threshold', th)
cv2.imshow('belirli (contours)', img_copy)
cv2.imshow('morph', morph)
cv2.imshow('dilate', dt)
cv2.imshow('threshold_2 (distance merkez)', th2)
cv2.imshow('toplam_th (merkez dişi)', cv2.subtract(th2, th))  # veya topla
cv2.imshow('markers (binarized)', marker_mask)
cv2.imshow('watershed kontur', img_copy1)

cv2.waitKey(0)
cv2.destroyAllWindows()
