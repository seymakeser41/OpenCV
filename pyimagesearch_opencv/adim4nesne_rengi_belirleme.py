"""
OPENCV İLE NESNE RENGİNİ BELİRLEME: 
-rengini belirlerken L*a*b* kanalı kullanılır çünkü renkler arasındaki Öklid mesafesini daha iyi ifade eder , en az öglid mesafesi olan rengi bulur 
"""
#BU KOD SAYFASI adim4nesne_rengi_belirleme_kod.py dosyasında kullanılacaktır
#gerekli paketleri import ettik
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2

class ColorLabeler:
    def __init__(self):
        # Renkleri içeren renk sözlüğünü başlatın
        colors = OrderedDict({
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255)
        })
        
        # L*a*b* görüntüsü için bellek ayırın, ardından isimleri tutacağı listeyi başlatın
        self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
        self.colorNames = []
        
        # Renk sözlüğü üzerinde döngü
        for i, (name, rgb) in enumerate(colors.items()):
            # L*a*b* dizisini ve renk adları listesini güncelleyin
            self.lab[i] = rgb
            self.colorNames.append(name)
        
        # RGB renk alanından L*a*b* dizisini dönüştürün
        self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)
    
    def label(self, image, c):
        # Kontur için bir maske oluşturun, konturları çizin, erozyana uğratın
        mask = np.zeros(image.shape[:2], dtype="uint8")
        cv2.drawContours(mask, [c], -1, 255, -1)
        mask = cv2.erode(mask, None, iterations=2)
        
        # Maskelenmiş bölge için ortalama L*a*b* değerini hesaplayın
        mean = cv2.mean(image, mask=mask)[:3]
        
        # Minimum mesafeyi tutacak değişken
        minDist = (np.inf, None)
        
        # Bilinen L*a*b renk değerleri üzerinde bir döngü
        for i, row in enumerate(self.lab):
            # Mevcut L*a*b renk değeri arasındaki mesafeyi hesaplayın
            d = dist.euclidean(row[0], mean)
            
            # Mesafe mevcut minimum mesafeden küçükse değeri güncelleyin
            if d < minDist[0]:
                minDist = (d, i)
        
        # Mesafesi en küçük olan rengin adını döndürün
        return self.colorNames[minDist[1]]
