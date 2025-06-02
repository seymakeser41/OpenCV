import cv2 
import numpy as np
import matplotlib.pyplot as plt

#histogram= gruplandırılmış veri dağılımının sütun grafiğinde gösterilmiş halidir 

img_duvar=cv2.imread(r"C:\Users\seyma\Desktop\media\duvar.jpg")
img_gok=cv2.imread(r"C:\Users\seyma\Desktop\media\gokkusagi.jpeg")
img_at=cv2.imread(r"C:\Users\seyma\Desktop\media\at.jpg")
# resmin ilk kanalının ağırlığını gösteren histogram grafiği oluşturulur
hist=cv2.calcHist([img_duvar],channels=[0],mask=None, histSize=[256],ranges=[0,256])
#tüm renk kanallarını sıraladık
color=('r','g','b')
#3 renk kanalının da sırasıyla histogramını oluşturması için döngü oluşturduk
for i,col in enumerate(color):
    histr=cv2.calcHist([img_duvar],[i], None, [256],[0,256])
    plt.plot(histr)
    plt.xlim([0,255]) #değerler hangi aralıkta
plt.title('HISTOGRAM') #tabloya başlık ekledik
plt.show()

#gösterme işlemleri
cv2.imshow('duvar', img_duvar)
cv2.imshow('gokkusagi',img_gok)
cv2.imshow('at', img_at)

plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
