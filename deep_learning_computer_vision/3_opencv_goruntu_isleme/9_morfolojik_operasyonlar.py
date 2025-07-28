import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread(r"C:\Users\seyma\Desktop\media\balls.jpg", 0)
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.title("Orijinal Img")

# erozyon
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations=1)
plt.figure(), plt.imshow(result, cmap="gray"), plt.axis("off"), plt.title("Erozyon")

# genişleme
result2 = cv2.dilate(img, kernel, iterations=1)
plt.figure(), plt.imshow(result2, cmap="gray"), plt.axis("off"), plt.title("Genisleme")

# white noise
whiteNoise = np.random.randint(0, 2, size=img.shape[:2]) * 255
plt.figure(), plt.imshow(whiteNoise, cmap="gray"), plt.axis("off"), plt.title("White Noise")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("Img w White Noise")

# açılma
opening = cv2.morphologyEx(noise_img.astype(np.uint8), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.title("Acilma")

# black noise
blackNoise = np.random.randint(0, 2, size=img.shape[:2]) * -255
plt.figure(), plt.imshow(blackNoise, cmap="gray"), plt.axis("off"), plt.title("Black Noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap="gray"), plt.axis("off"), plt.title("Black Noise Img")

# kapama
closing = cv2.morphologyEx(black_noise_img.astype(np.uint8), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap="gray"), plt.axis("off"), plt.title("Kapama")

# gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("Gradyan")

# GÖSTER!
plt.show()
