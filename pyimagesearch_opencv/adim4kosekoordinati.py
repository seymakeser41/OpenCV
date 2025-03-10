import cv2
import numpy as np

# Resmi yükle
image = cv2.imread(r"C:\Users\seyma\Desktop\media\yamuk_resim.png")

# HSV renk uzayına dönüştür
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Yeşil renk için alt ve üst sınırları belirle
lower_green = np.array([40, 40, 40])
upper_green = np.array([90, 255, 255])

# Maske oluştur
mask = cv2.inRange(hsv, lower_green, upper_green)

# Konturları bul
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Koordinatları saklamak için liste
coordinates = []

for contour in contours:
    if cv2.contourArea(contour) > 5:  # Küçük gürültüleri ele
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            coordinates.append((cx, cy))

# Koordinatları yazdır
print("Yeşil noktaların koordinatları:", coordinates)

# Sonucu göster (isteğe bağlı)
for (x, y) in coordinates:
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

cv2.imshow("Detected Points", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
