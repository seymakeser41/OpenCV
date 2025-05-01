# gerekli paketleri içeri aktar 
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,help="path to the output image")
args = vars(ap.parse_args())

# resim yollarını sıralayın ve resimler için dizi oluşturun
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []
# görüntü yolları üzerinde döngü yapın, her birini yükleyin ve bunları birleştirin
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	images.append(image)
	
# OpenCV'nin görüntü birleştirici nesnesini başlatın ve ardından görüntüyü birleştirin
print("[INFO] stitching images...")
stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

# durum '0' ise, OpenCV görüntü birleştimeyi başarıyla gerçekleştirildi
if status == 0:
	# Çıktı dikişli görüntüyü diske yazın
	cv2.imwrite(args["output"], stitched)
	# Çıktı dikişli görüntüyü ekranımızda görüntüleyin
	cv2.imshow("Stitched", stitched)
	cv2.waitKey(0)
# aksi takdirde, muhtemelen yeterli anahtar nokta olmaması nedeniyle dikiş başarısız oldu
else:
	print("[INFO] image stitching failed ({})".format(status))