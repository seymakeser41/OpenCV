# gerekli paketler içeri aktarılır
from adim4perspektif_dönüsümü import four_point_transform
import numpy as np
import argparse
import cv2

# argüman ayrıştırıcı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-c", "--coords",help = "comma seperated list of source points")
args = vars(ap.parse_args())
# resmi yükle , kaynak koordinatları al 
#NOT: 'eval' işlevini kullanmak kötü bir biçimdir, ancak bu örnek için sorun olmayacaktır
image = cv2.imread(args["image"])
pts = np.array(eval(args["coords"]), dtype = "float32")
# kuş bakışı görünüm için transform uygulanır
warped = four_point_transform(image, pts)
# resimleri görüntüleyin
cv2.imshow("Original", image)
cv2.imshow("Warped", warped)
cv2.waitKey(0)