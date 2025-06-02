import cv2
import numpy as np

# Köşe tespiti için gerekli parametreler
corner_track_params = dict(
    maxCorners=10,         # En fazla 10 köşe tespit edilsin
    qualityLevel=0.3,      # Kalite oranı (yüksek kalite için düşük değer)
    minDistance=7,         # Köşeler arası minimum mesafe
    blockSize=7            # Köşe algılamada kullanılacak bölge boyutu
)

# Optik akış (Lucas-Kanade) için parametreler
lk_params = dict(
    winSize=(200, 200),  # Pencere boyutu (büyük değer: daha sağlam takip)
    maxLevel=2,          # Piramit seviyeleri
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)  # Durdurma kriteri
)

# Kamerayı başlat
cap = cv2.VideoCapture(0)

# Kamera açılamadıysa çık
if not cap.isOpened():
    print("Kamera açılamadı.")
    exit()

# İlk kareyi oku
ret, prev_frame = cap.read()
if not ret:
    print("Kamera görüntüsü alınamadı.")
    cap.release()
    exit()

# İlk kareyi gri tona çevir
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# İlk karede köşe noktalarını tespit et
points = cv2.goodFeaturesToTrack(prev_gray, mask=None, **corner_track_params)

# Çizim için boş bir maske oluştur (aynı boyutta)
mask = np.zeros_like(prev_frame)

while True:
    # Yeni kareyi al
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı.")
        break

    # Yeni kareyi gri tona çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lucas-Kanade yöntemiyle köşeleri takip et
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(prev_gray, gray, points, None, **lk_params)

    # Takibi başarıyla yapılan noktaları ayıkla
    good_new = nextPts[status == 1]
    good_prev = points[status == 1]

    # Tüm başarılı eşleşmeleri çiz
    for i, (new, prev) in enumerate(zip(good_new, good_prev)):
        x_new, y_new = map(int, new.ravel())     # Yeni nokta koordinatları
        x_prev, y_prev = map(int, prev.ravel())  # Eski nokta koordinatları

        # Hareket yönünü çiz (çizgi)
        mask = cv2.line(mask, (x_prev, y_prev), (x_new, y_new), (255, 0, 0), 3)

        # Yeni noktaya daire koy
        frame = cv2.circle(frame, (x_new, y_new), 8, (0, 0, 255), -1)

    # Maskeyi ve orijinal görüntüyü birleştir
    img = cv2.add(frame, mask)

    # Sonucu göster
    cv2.imshow('Optik Akiş Takibi (q ile çik)', img)

    # Çıkmak için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Bir sonraki kare için güncelleme yap
    prev_gray = gray.copy()
    points = good_new.reshape(-1, 1, 2)

# Kamera ve pencereyi kapat
cap.release()
cv2.destroyAllWindows()
