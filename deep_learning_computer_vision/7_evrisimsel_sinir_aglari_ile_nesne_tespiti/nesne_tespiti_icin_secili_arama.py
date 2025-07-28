"""
süper piksel algoritmasi kullanarak görseli asiri bölümlere ayirma 
süper piksel: ortak özellikleri paylaşan bir piksel grubu 
5 temel özellikle pikselleri birleştirir:
-renk , doku, boyut, şekil, ve hepsinin benzerliklerinin doğrusal kombinasyonu
sinif etiketi değil bölgeler oluşturur

"""


import cv2
import random

image = cv2.imread(r"C:\Users\seyma\Desktop\media\pyramid.jpg")
image = cv2.resize(image, dsize = (600,600))
cv2.imshow("image",image)

# ilklendir ss
ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation() #segmantasyon algoritması
ss.setBaseImage(image)
ss.switchToSelectiveSearchQuality()

print("start")
rects = ss.process() #dikdörtgenleri oluşturuyor

output = image.copy()

#dikdörtgenleri görselleştirme
for (x,y,w,h) in rects[:50]:
    color = [random.randint(0,255) for j in range(0,3)]
    cv2.rectangle(output, (x,y),(x+w,y+h),color,2)
    
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()