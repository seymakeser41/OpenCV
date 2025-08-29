#10_DATASET_TOPLAMA
"""
tespit etmek istenilen nesne ile ilgili resim topla ve bir klasöre kaydet"""

#11_DATASETİ DÜZENLEME 

#tüm resimleri jpg formatına getirme
"""
import cv2
import os
from glob import glob

png = glob(r"C:\Users\seyma\Desktop\media\custom_yolo_model\spot_data\images\*.png")

for j in png:
    print(j)
    img = cv2.imread(j)
    cv2.imwrite(j[:-4]+"jpg",img)
    os.remove(j)
"""
    
#12_RESİMLERİ_ETİKETLEME
"""
makesense.ia 
resimlerin olduğu klasörü aç 
tek tek resimler üstünde etiketleme yap
export label diyerek tüm etiketleri indir
labelleri imageslerla ayni klasöre taşi
"""


#13_EĞİTİM_VE_TEST_VERİLERİNİ_DÜZENLEME

"""
import re
from pathlib import Path

# >>> Düzenlenecek Kısımlar <<<
ornek_yol    = r"C:\Users\seyma\Desktop\media\custom_yolo_model\spot_data\spot_images\1.jpg"  # Yol (prefix ve uzantıyı almak için sadece örnek)
start_num    = 321                           # Başlangıç değeri (buradan başlar)
adet         = 80                          # Kaç satır üretilecek
cikis_dosyasi = r"C:\Users\seyma\Desktop\media\custom_yolo_model\spot_data\spot_testing.txt"    # Çıktı metin dosyası

# Regex ile prefix, sayı uzunluğu ve uzantıyı ayır
m = re.search(r"^(.*?)(\d+)(\.[^.\\/]+)$", ornek_yol)
if not m:
    raise ValueError("Dosya adında uzantıdan hemen önce bir sayı bulunamadı.")

prefix, numstr, ext = m.groups()
pad = len(numstr)  # Sıfır doldurma genişliği (örn. 0001 -> 4)

# Satırları oluştur
satirlar = []
for i in range(adet):
    n = start_num + i  # başlangıçtan itibaren 1’er artış
    yeni_yol = f"{prefix}{n:0{pad}d}{ext}"
    satirlar.append(yeni_yol)

# Dosyaya yaz
Path(cikis_dosyasi).write_text("\n".join(satirlar), encoding="utf-8")
print(f"{len(satirlar)} satır yazıldı -> {cikis_dosyasi}")
"""

#bu kod ile öncelikle test ve train olarak resimleri ayır %20 oranla