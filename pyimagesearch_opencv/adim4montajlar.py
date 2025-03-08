"""
1- diskteki görüntü kümesinden grüntü yollarinin bir listesini oluşturma  -->build_montages(3 parametre: image_list, image_shape, montage_shape)
2- montaji ekranda göster
"""

# gerekli paketleri içe aktar
from imutils import build_montages
from imutils import paths
import argparse
import random
import cv2

#argüman ayrıştırıcılarını oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,help="path to input directory of images")
ap.add_argument("-s", "--sample", type=int, default=21,help="# of images to sample")
args = vars(ap.parse_args())

# Görüntülere giden yolları alın, ardından içlerinden rastgele bir örnek seçin
imagePaths = list(paths.list_images(args["images"]))
random.shuffle(imagePaths)
imagePaths = imagePaths[:args["sample"]]


# Görüntü listesini oluşturun
images = []
# Görüntü yolları listesi üzerinde döngü oluşturun
for imagePath in imagePaths:
	# Resmi yükleyin ve resim listesini güncelleyin
	image = cv2.imread(imagePath)
	images.append(image)
# Görüntüler için montajları oluşturun
montages = build_montages(images, (128, 196), (7, 3))

# montajların üzerinden gezinin ve her birini görüntüleyin
for montage in montages:
	cv2.imshow("Montage", montage)
	cv2.waitKey(0)