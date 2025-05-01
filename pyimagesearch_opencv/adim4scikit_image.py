"""
-->scikit-image ve python ile eşleşen histogram :
iki görüntünün renk dağılımını (kontrast) eşleştirmek için
1. her görüntü için hidtogram hesaplanır 
2. referans görüntünün hidtogramını alın
3. referans histogramları kullanarak giriş görüntüsündeki piksel yoğunluğu değerlerini, eşleşecek şekilde güncelleyin

histogram eşitleme: bir görüntünün piksel yoğunluklarını refesans görüntü histogram dağılımına göre güncellemek . gerçek içerik değişmez piksel dağılımı gerçekleşir . hem tek kanallı hem çok kanallı görüntüde uygulanabilir.
-scikit-image kullanarak match_histograms fonksiyonu kullanmak kolaylık sağlar. pip ile yüklenir 


"""
#kütüphaneleri ve gerekli paketleri import ettik
from skimage import exposure #histogram eşitlemeyi uygulamak için gerekli
import matplotlib.pyplot as plt  #histogram görüntülemek için gerekli
import argparse
import cv2
# argparse kullanarak argüman ayrıştırıcısı oluşturun ve argümanları ayrıştırın
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--source", required=True,help="path to the input source image")
ap.add_argument("-r", "--reference", required=True,help="path to the input reference image")
args = vars(ap.parse_args())


# Kaynak ve referans görüntüleri yükleyin
print("[INFO] loading source and reference images...")
src = cv2.imread(args["source"])
ref = cv2.imread(args["reference"])
# Çok kanallı histogram eşleştirmesi yapıp yapmadığımızı belirleyin
# histogram eşleştirmesini kendisi gerçekleştirir
print("[INFO] performing histogram matching...")
multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, channel_axis=-1)


cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)

# histogram eşleştirmesi uygulanmadan önce ve sonra her kanal için histogram çizimlerini görüntülemek için bir şekil oluşturun
(fig, axs) =  plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
# Kaynak görüntümüz, referans görüntümüz ve eşleşen çıktımız üzerinde döngü yapın
for (i, image) in enumerate((src, ref, matched)):
	# görüntüyü BGR'den RGB kanal sıralamasına dönüştürün
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# RGB sırasına göre kanalların adları üzerinde döngü yapın
	for (j, color) in enumerate(("red", "green", "blue")):
		#  Geçerli kanal için bir histogram hesaplayın ve çizin
		(hist, bins) = exposure.histogram(image[..., j],source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())
		# mevcut kanal ve çizin için kümülatif dağılım fonksiyonunu hesaplayın
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)
		# Geçerli renk kanalının geçerli grafiğin Y ekseni etiketini ad olarak ayarlayın
		axs[j, 0].set_ylabel(color)


# eksen başlıklarını ayarlayın
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")
# çıktı grafiklerini görüntüleyin
plt.tight_layout()
plt.show()


cv2.waitKey(0)


