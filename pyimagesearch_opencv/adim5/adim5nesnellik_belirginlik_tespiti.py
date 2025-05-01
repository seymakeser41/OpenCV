# gerekli paketleri içeri aktar
import numpy as np
import argparse
import cv2
# argüman ayrıştırıcı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,help="path to BING objectness saliency model")
ap.add_argument("-i", "--image", required=True,help="path to input image")
ap.add_argument("-n", "--max-detections", type=int, default=10,help="maximum # of detections to examine")
args = vars(ap.parse_args())
#resmi yükle
image = cv2.imread(args["image"])

# OpenCV'nin nesnellik belirginlik dedektörünü başlatın
#giriş modeli dosyalarına yolu ayarlayın
saliency = cv2.saliency.ObjectnessBING_create()
saliency.setTrainingPath(args["model"])
# belirginliği belirtmek için kullanılan sınırlayıcı kutu tahminlerini hesaplayın
(success, saliencyMap) = saliency.computeSaliency(image)
numDetections = saliencyMap.shape[0]

# algılamalar üzerine döngü
for i in range(0, min(numDetections, args["max_detections"])):
	# Sınırlayıcı kutu koordinatlarını çıkarın
	(startX, startY, endX, endY) = saliencyMap[i].flatten()
	
	# Nesne için rastgele bir renk oluşturun ve görüntünün üzerine çizin
	output = image.copy()
	color = np.random.randint(0, 255, size=(3,))
	color = [int(c) for c in color]
	cv2.rectangle(output, (startX, startY), (endX, endY), color, 2)
	# çıktıyı görüntüle
	cv2.imshow("Image", output)
	cv2.waitKey(0)