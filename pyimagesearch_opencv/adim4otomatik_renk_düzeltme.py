"""
--> otomatik renk düzeltme :
renk sabitliği yoluyla renk düzenlemesi yapmaktır. farklı koşullarda doğru rengi tespit etme 
1. giriş görüntüdeki renk düzenleme kartını algıla
2. farklı renklerde , tonlarda,gölgelerde,siyahlarda,beyazlarda derecelendirilmiş renkler içeren kartın histogramını hesapla
3. renk kartlarından başka bir görüntüye histogram eşitlemesi uygulayın, renk sabitliği elde edin 
"""
#ArUco işaretleyicilerini-----> başka dosyada
#Kontrast Sınırlı Uyarlanabilir Histogram Eşitleme (CLAHE) ------> başka dosya
#OpenCV, scikit-image ve Python ile eşleşen histogram -----> başka dosyada 

# gerekli paketler içeri aktarılır
from imutils.perspective import four_point_transform
from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2
import sys

def find_color_card(image):
    # ArUCo sözlüğünü yükleyin, ArUCo parametrelerini alın ve giriş görüntüsündeki işaretçileri algıla
    arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)
    arucoParams = cv2.aruco.DetectorParameters()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
    
    # Renk düzeltme kartının koordinatlarını çıkarmaya çalışın
    try:
        # Aksi takdirde, dört ArUco işaretçisini bulduk, böylece yapabiliriz
        # ArUco IDS listesini düzleştirerek devam edin
        ids = ids.flatten()
        
        # Sol üst işaretçiyi çıkarın
        i = np.squeeze(np.where(ids == 923))
        topLeft = np.squeeze(corners[i])[0]
        
        # Sağ üstteki işaretçiyi çıkarın
        i = np.squeeze(np.where(ids == 1001))
        topRight = np.squeeze(corners[i])[1]
        
        # Sağ alttaki işaretçiyi çıkarın
        i = np.squeeze(np.where(ids == 241))
        bottomRight = np.squeeze(corners[i])[2]
        
        # Sol alttaki işaretçiyi çıkarın
        i = np.squeeze(np.where(ids == 1007))
        bottomLeft = np.squeeze(corners[i])[3]
        
    except:
        return None
    
    # Referans noktaları listemizi oluşturun ve perspektif dönüşümünü uygulayın
    cardCoords = np.array([topLeft, topRight, bottomRight, bottomLeft])
    card = four_point_transform(image, cardCoords)
    
    return card

# Argüman ayrıştırıcısını oluşturun ve argümanları ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--reference", required=True, help="path to the input reference image")
ap.add_argument("-i", "--input", required=True, help="path to the input image to apply color correction to")
args = vars(ap.parse_args())

# Referans görüntüyü ve giriş görüntüsünü yükleyin
print("[INFO] loading images...")
ref = cv2.imread(args["reference"])
image = cv2.imread(args["input"])

# Referans ve giriş resimlerini yeniden boyutlandırın
ref = imutils.resize(ref, width=600)
image = imutils.resize(image, width=600)

# Referans ve giriş resimlerini gösterin
cv2.imshow("Reference", ref)
cv2.imshow("Input", image)

# Her iki görüntüde de renk eşleştirme kartını bulun
print("[INFO] finding color matching cards...")
refCard = find_color_card(ref)
imageCard = find_color_card(image)

# Renk eşleştirme kartı bulunamazsa programı sonlandır
if refCard is None or imageCard is None:
    print("[INFO] could not find color matching card in both images")
    sys.exit(0)

# Referans görüntüde ve giriş görüntüsünde renk eşleştirme kartını gösterin
cv2.imshow("Reference Color Card", refCard)
cv2.imshow("Input Color Card", imageCard)

# Histogram eşleştirmesini uygula
print("[INFO] matching images...")
imageCard = exposure.match_histograms(imageCard, refCard, channel_axis=-1)


# Eşleştirme sonrası görüntüyü göster
cv2.imshow("Input Color Card After Matching", imageCard)
cv2.waitKey(0)