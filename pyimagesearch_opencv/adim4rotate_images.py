"""
OPENCV VE PYTHON İLE GÖRÜNTÜLERİ DOĞRU DÖNDÜRÜN
-Döndürürken kesintiler olabilir 
-rotated = imutils.rotate_bound(görüntü, açı))
-$ python rotate_simple.py --image images/saratoga.jpg
ile görüntüyü döndürürken tam olarak alır
"""
#kütüphaneler eklenir
import numpy as np
import imutils
import cv2
#argparse kullanarak resmi dahil etme işlemi
"""
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to the image file")
args = vars(ap.parse_args())
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())
"""
#resmi dahil ettik
image = cv2.imread(r"C:\Users\seyma\Desktop\media\tetris.png") 
cv2.imshow("Image", image)
#döngü açıları üzerinden sürekli bir döngü sağlar
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate(image, angle) #sadece görüntüyü döndürür fazlalıkları önemsemez
	cv2.imshow("Rotated (Problematic)", rotated)
	cv2.waitKey(100)

#görüntüyü döndürürken kayıp yaşanabilcek durumları gözetip tamamen döndürür
for angle in np.arange(0, 360, 15):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imshow("Rotated (Correct)", rotated)
	cv2.waitKey(100)
	

def rotate_bound(image, angle):
    # görüntünün boyutlarına göre merkezini bulun
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # dönme matrisini oluşturun ve dönme bileşenerini( cos ve sin) alın
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # yeni sınırlayıcı boyutları hesaplayın
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # çeviriyi hesaba katarak dönme matrisini ayarlayın
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # dönüşü gerçekleştirin 
    return cv2.warpAffine(image, M, (nW, nH))
cv2.imshow("Rotated (fonkcion)", image)
cv2.waitKey(0)
    