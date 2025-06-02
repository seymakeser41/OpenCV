import cv2
import numpy as np
import matplotlib.pyplot as plt

#Görselleri yükle
chess_board = cv2.imread(r"C:\Users\seyma\Desktop\media\satranc.jpg")       # Satranç tahtası resmi
chess = cv2.imread(r"C:\Users\seyma\Desktop\media\satranc1.jpeg")           # Gerçek çekilmiş satranç fotoğrafı

# Görsellerin kopyasını al (orijinalleri korumak için)
chess1 = chess_board.copy()
chess2 = chess.copy()

#Görselleri gri tonlamaya çevir (köşe tespiti için gereklidir)
gray1 = cv2.cvtColor(chess1, cv2.COLOR_RGB2GRAY)
gray2 = cv2.cvtColor(chess2, cv2.COLOR_RGB2GRAY)

# Gri görüntüyü float32 formatına çevir (Harris algoritması bu formatı ister)
gray_1 = np.float32(gray1)
gray_2 = np.float32(gray2)

#Harris Corner Detection (Satranç tahtası resmi için)
dst = cv2.cornerHarris(gray_1, blockSize=2, ksize=3, k=0.04)  # Köşe tespiti: küçük bloklarda yüksek varyans
dst = cv2.dilate(dst, None)                                   # Köşe tespitlerini genişlet (daha belirgin gösterim)
chess1[dst > 0.01 * dst.max()] = [255, 0, 0]                  # Güçlü köşeleri kırmızı renkle işaretle

# Harris Corner Detection (Gerçek satranç fotoğrafı için)
dst_1 = cv2.cornerHarris(gray_2, 2, 3, 0.04)
dst_1 = cv2.dilate(dst_1, None)
chess2[dst_1 > 0.01 * dst_1.max()] = [255, 0, 0]

#  goodFeaturesToTrack fonksiyonu ile köşe tespiti (chess_board için)
# Bu fonksiyon en belirgin N tane köşeyi bulur
corners = cv2.goodFeaturesToTrack(gray1, maxCorners=5, qualityLevel=0.01, minDistance=10)
corners = np.int8(corners)  # Noktaları tam sayıya çevir

# Bulunan köşe noktalarına daire çiz (chess1 üzerinde)
for i in corners:
    x, y = i.ravel()  # (x,y) koordinatlarını çıkar
    cv2.circle(chess1, (x, y), 3, 255, -1)  # Küçük daire çiz
    cv2.imshow('good_features', chess1)    # Her çember çizildiğinde resmi göster (gereksiz tekrar olabilir)

# Aynı köşe tespitini tekrar yap (gray2 üzerinde  çalışılıyor )
corners1 = cv2.goodFeaturesToTrack(gray2, 5, 0.01, 10)
corners1 = np.int8(corners1)

# Bulunan köşelere daire çiz (chess2 üzerinde)
for i in corners1:
    x, y = i.ravel()
    cv2.circle(chess2, (x, y), 3, 255, -1)
    cv2.imshow('good_features_2', chess2)  # Her adımda gösteriliyor (bu da tekrar olabilir)


cv2.imshow('satranc_tahtasi', chess_board)    # Orijinal satranç tahtası
cv2.imshow('satranc', chess)                  # Gerçek çekilen fotoğraf
cv2.imshow('gri1', gray1)                     # İlk görüntünün gri hali
cv2.imshow('gri2', gray2)                     # İkinci görüntünün gri hali
cv2.imshow('koseli_tahta', chess1)            # Harris + goodFeaturesToTrack ile işaretlenmiş tahta
cv2.imshow('real_koseli', chess2)             # Gerçek fotoğrafın köşe tespitli hali


cv2.waitKey(0)
cv2.destroyAllWindows()
