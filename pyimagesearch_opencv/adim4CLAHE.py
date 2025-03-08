"""
--> OpenCV histogram eşitleme ve uyarlanabilir histogram eşitleme (CLAHE) :
histogam eşitleme:
1. görüntü piksel yoğunluklarinin histogramini hesaplama 
2. en cok kullanilan piksel değelerini(histogramda en büyük sayiya sahip)  eşit olarak yayma ve dağıtma 
3. kümülatif dağilim fonksiyonu (CDF) doğrusal bir eğilim verme 

Kontrast Sinirli Uyarlanabilir Histogram Eşitleme (CLAHE) algoritma kullanarak histogram eşitlemeyi daha iyi hal getirir 

uygulamali histogram eşitleme :
1. giriş görüntüsü gri tonlamaya dönüştürün , ondan tek bir kanal çikarin --> cv2.equalizeHist
2. CLAHE algoritmaini kullanarak örnekleyin ---> cv2.createCLAHE
3. uygulayin -->apply
"""

# gerekli paketleri içeri aktar
import argparse
import cv2
# argüman ayrıştırıcıyı oluştur ve ayrıştır
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,help="path to the input image")
args = vars(ap.parse_args())

# resmi yükle ve gri moda çevir
print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# histogram eşitlemeyi uygula
print("[INFO] performing histogram equalization...")
equalized = cv2.equalizeHist(gray)

#çıktıları görüntüle 
cv2.imshow("Input", gray)
cv2.imshow("Histogram Equalization", equalized)
cv2.waitKey(0)