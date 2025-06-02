import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\internal.png")
gray1=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# bu fonksiyonla contourlar bulunur ve değerleri hierarchy değişkeninde tututlur
contours, hierarchy= cv2.findContours(gray1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
#bu noktaları görüntülemek amaçlı bir ekran oluştudu
external_contours= np.zeros_like(gray1)

#contourlar üzerinde dolaşarak çizim işlemi yapacağız 
for i in range(len(contours)):
    if hierarchy[0][i][3]==-1: #external noktalar bu şekilde ayırt edilir(iç noktalar dışındaki alanlar)
        cv2.drawContours(external_contours, contours, i, 255,-1)

# bu işlemleri iç noktalar için tekrarladık
image_internal=np.zeros_like(gray1)
for i in range(len(contours)):
    if hierarchy[0][i][3]!=-1: #internal noktalar bu şekilde ayırt edilir(iç noktalar )
        cv2.drawContours(image_internal, contours, i, 255,-1)

#görselleştirmeler
cv2.imshow('internal', img)
cv2.imshow('gri1', gray1)
cv2.imshow('external',external_contours) #iç noktaları almadan
cv2.imshow('internal', image_internal) #iç noktaları çizer
cv2.waitKey(0)
cv2.destroyAllWindows()