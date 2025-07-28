"""
- veri setini bul https://motchallenge.net/data/MOT17/ 
- veri seti indir  veri setini indir ve videoyu oluşturan resimleri olduğu klasör ve
 gt.txt dosyasini veri seti oluşturmada kullanabilmek için bir yere taşi 
- resimleri videoya çevir
- eda -> gt
"""
"""

gt.txt dosyası içeriği (9 adet veri)
1-frame numarası
2-identity number (kutu numarası )
3-kutunu sol kenarı
4-kutunun üst  kenarı
5-kutunu genişliği
6-kutunun yüksekliği
7-ne kadar göründüğü
8-sınıfı
9-görünürlüğü
"""
import cv2
import os
from os.path import isfile, join
import matplotlib.pyplot as plt

pathIn = r"C:\Users\seyma\Desktop\media\img1"
pathOut = r"C:\Users\seyma\Desktop\media\MOT17-13-SDP.mp4"

files = [f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]


fps = 25
size = (1920,1080)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*"MP4V"), fps, size, True)

for i in files:
    print(i)
    
    filename = pathIn + "\\" + i
    
    img = cv2.imread(filename)
    
    out.write(img)

out.release()
