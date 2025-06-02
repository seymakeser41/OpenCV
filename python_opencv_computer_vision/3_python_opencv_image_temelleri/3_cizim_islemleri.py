import cv2
import numpy as np

# Başlangıçta tamamen siyah bir tuval oluştur (RGB: 0,0,0)
bos = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

# 1. Adım: sadece siyah ekran
cv2.imshow('bos', bos)
cv2.waitKey(0)

# 2. Adım: dikdörtgen çiz
dik = bos.copy()
cv2.rectangle(dik, (300, 100), (400, 300), (255, 0, 0), 7)
cv2.imshow('dikdortgen', dik)
cv2.waitKey(0)

# 3. Adım: kare çiz
kare = dik.copy()
cv2.rectangle(kare, (200, 200), (300, 300), (0, 255, 0), 7)
cv2.imshow('kare', kare)
cv2.waitKey(0)

# 4. Adım: daire çiz
daire = kare.copy()
cv2.circle(daire, (100, 100), 50, (0, 255, 255), -1)
cv2.imshow('daire', daire)
cv2.waitKey(0)

# 5. Adım: çizgi çiz
cizgi = daire.copy()
cv2.line(cizgi, (0, 0), (512, 512), (255, 0, 0), 7)
cv2.imshow('cizgi', cizgi)
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
