"""
Laplacian'in Varyansi:Bir görüntünün tek bir kanalını (muhtemelen gri tonlamalı) alır ve aşağıdaki 3 x 3 çekirdekle birleştirirsiniz
Ve sonra yanıtın varyansını (yani standart sapmanın karesini) alın.
Varyans önceden tanımlanmış bir eşiğin altına düşerse, görüntü bulanık olarak kabul edilir; aksi takdirde görüntü bulanık olmaz.
Laplacian, Sobel ve Scharr operatörleri gibi, bir görüntünün hızlı yoğunluk değişiklikleri içeren bölgelerini vurgular.
Ve tıpkı bu operatörler gibi, Laplacian da genellikle kenar tespiti için kullanılır.
Eşik çok düşükse ve görüntüleri bulanık olmadıkları halde yanlış bir şekilde bulanık olarak işaretlersiniz. Eşik çok yüksekse, gerçekten bulanık olan görüntüler bulanık olarak işaretlenmez.

"""

# gerekli paketleri içeri aktar
from imutils import paths
import argparse
import cv2
def variance_of_laplacian(image):
	# görüntünün Laplacian'ını hesaplayın ve ardından Laplace'nin varyansı olan ölçüye odaklanın
	return cv2.Laplacian(image, cv2.CV_64F).var()
# argüman ayrıştırıcıyı oluşturun ve ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,help="path to input directory of images")
ap.add_argument("-t", "--threshold", type=float, default=100.0,help="focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

# listedeki resimlerin yoları üzerinde döngü
for imagePath in paths.list_images(args["images"]):
	# resmi yükleyin, gri formata çevirin, Laplacian methodunun varyansını kullanarak resmin odak ölçüsünü hesaplayn
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	text = "Not Blurry"
	# Odak ölçüsü sağlanan eşikten düşükse,o zaman görüntü "bulanık" olarak kabul edilmelidir
	if fm < args["threshold"]:
		text = "Blurry"
	# resmi göster, bulanıklığı belirt
	cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
	cv2.imshow("Image", image)
	key = cv2.waitKey(0)