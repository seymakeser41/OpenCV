"""
OpenCV'lerde belirginlik Modül Belirginlik algılamanın üç temel biçimi vardır:

Statik belirginlik: Bu belirginlik algılama algoritmaları sınıfı, bir görüntünün en ilginç bölgelerini yerelleştirmek için görüntü özelliklerine ve istatistiklere dayanır.
Hareket belirginliği: Bu sınıftaki algoritmalar genellikle video veya kare kare girişlere dayanır. Hareket belirginliği algoritmaları, "hareket eden" nesneleri takip ederek kareleri işler. Hareket eden nesneler göze çarpan olarak kabul edilir.
Nesnellik: "Nesnelliği" hesaplayan belirginlik algılama algoritmaları, bir dizi "teklif" veya daha basit bir şekilde, bir nesnenin bir görüntüde olabileceğini düşündüğü yerin sınırlayıcı kutularını oluşturur.

OpenCV bize Python bağlamaları ile dört belirginlik dedektörü uygulaması sağlar:
cv2.saliency.ObjectnessBING_create()
cv2.saliency.StaticSaliencySpectralResidual_create()
cv2.saliency.StaticSaliencyFineGrained_create()
cv2.saliency.MotionSaliencyBinWangApr2014_create()

Bu yöntemleri giriş görüntümüzde çağırırız ve iki demet döndürürüz:

Belirginliğin hesaplanmasının başarılı olup olmadığını gösteren bir boole
Bir görüntünün en "ilginç" bölgelerini türetmek için kullanabileceğimiz çıktı belirginlik haritası
"""
# gerekli paketleri içeri aktar
import argparse
import cv2
# argüman ayrıştırıcıları oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,help="path to input image")
args = vars(ap.parse_args())
# giriş resmi yükle
image = cv2.imread(args["image"])

# OpenCV'nin statik belirginlik spektural kalıntılı dedektörünü başlatın
# belirginlik haritasını hesaplayın
saliency = cv2.saliency.StaticSaliencySpectralResidual_create()
(success, saliencyMap) = saliency.computeSaliency(image)
saliencyMap = (saliencyMap * 255).astype("uint8")
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.waitKey(0)

# OpenCV'nin statik ince taneli belirginlik dedektörünü başlatın 
# belirginlik haritasını hesaplayın
saliency = cv2.saliency.StaticSaliencyFineGrained_create()
(success, saliencyMap) = saliency.computeSaliency(image)
# İzohipsler için işleyebileceğimiz *ikili* bir harita istersek,
# Dışbükey gövdeleri hesaplayabilir, sınırlayıcı kutuları çıkarabilir vb.
# ayrıca belirginlik haritasını eşikleyin
threshMap = cv2.threshold(saliencyMap.astype("uint8"), 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# resmi göster
cv2.imshow("Image", image)
cv2.imshow("Output", saliencyMap)
cv2.imshow("Thresh", threshMap)
cv2.waitKey(0)