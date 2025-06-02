#Farneback optik akış yöntemiyle hareketi tespit edip renkli bir şekilde görselleştirme
import cv2
import numpy as np

# Kamerayı başlat (0 = varsayılan kamera)
cap = cv2.VideoCapture(0)

# İlk kareyi oku
ret, frame1 = cap.read()

# İlk kareyi gri tonlamaya çevir (optik akış hesaplaması gri görüntü ile yapılır)
prev_img = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)

# HSV (Hue-Saturation-Value) renk uzayında bir boş maske oluştur
# Aynı boyutta 3 kanallı bir dizi, başta tüm kanallar 0
mask = np.zeros_like(frame1)

# Saturation (doygunluk) kanalını 255 yap (renkler tam doygunlukta gözüksün diye)
mask[:, :, 1] = 255

# Ana döngü: Her yeni karede hareketi tespit et
while True:
    # Yeni kareyi oku
    ret, frame = cap.read()
    if not ret:
        break

    # Yeni kareyi gri tonlamaya çevir
    next_img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Farneback algoritmasıyla yoğun (dense) optik akış hesapla
    flow = cv2.calcOpticalFlowFarneback(
        prev_img,         # önceki gri kare
        next_img,         # sonraki gri kare
        None,             # çıktı (akış vektörleri); None ise OpenCV otomatik oluşturur
        0.5,              # pyr_scale: her seviye için görüntü küçültme oranı
        3,                # levels: piramit katman sayısı
        15,               # winsize: pencere boyutu
        3,                # iterations: her seviyede yineleme sayısı
        5,                # poly_n: polinom genişliği
        1.2,              # poly_sigma: polinom sigma değeri
        0                 # flags: varsayılan değer
    )

    # Farneback algoritması, her pikselin hareketini bir vektörle verir (x, y bileşenleri)
    # Bu vektörlerin büyüklüğü (magnitude) ve yönü (angle) hesaplanır
    mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1], angleInDegrees=True)

    # Hue kanalını (H) yön bilgisiyle doldur (0–180 arası olmalı → 360° / 2)
    mask[:, :, 0] = ang / 2

    # Value kanalını (V) hareketin büyüklüğüyle doldur, [0–255] aralığına normalize et
    mask[:, :, 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

    # HSV formatındaki görüntüyü BGR formatına çevir (görselleştirme için)
    bgr = cv2.cvtColor(mask, cv2.COLOR_HSV2BGR)

    # Hareket yönü ve şiddetinin renkli olarak gösterildiği görüntüyü ekranda göster
    cv2.imshow('video', bgr)

    # 'q' tuşuna basılırsa çık
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    # Sonraki karede karşılaştırma için mevcut kareyi "önceki kare" olarak güncelle
    prev_img = next_img

# Kamera bağlantısını kapat ve pencereleri temizle
cap.release()
cv2.destroyAllWindows()
