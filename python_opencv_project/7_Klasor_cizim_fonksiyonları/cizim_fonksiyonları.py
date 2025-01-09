import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) +255 #tuval_olusturduk(siyah).ve_boyut_çizim yapabilmek için gerekli rakamı(renkli=3) ve tipi belirttik
#255 ekleyerek matris içindeki değerleri 0 dan 255 e çevirdik ve artık tuvalimiz beyaz

cv2.line(canvas,(50,50),(512,512),(255,0,0),thickness=5) #çizgi çizdik noktalar boyut renk ve kalınlık parametreleri ile
cv2.line(canvas,(100,50),(200,250),(0,0,255),thickness=7)

cv2.rectangle(canvas,(20,20),(50,50),(0,255,0),-1)#dikdörtgen çizme fonksiyonu alt köşeleri girdik rengi ve kalılığı -1 seçerek içini doldurduk
cv2.rectangle(canvas,(50,50),(150,150),(255,255,0),-1)

cv2.circle(canvas,(250,250),100,(0,0,255),thickness=-1)#çember çizme fonksiyonu merkez ve yarıçap, renk, kalınlık değerlerini girdik

#üçgen için ayrı bir fonk yok line kullanılacak
p1=(100,200)
p2=(50,50)
p3=(300,100)
cv2.line(canvas,p1,p2,(0,0,0),4)
cv2.line(canvas,p2,p3,(0,0,0),4)
cv2.line(canvas,p1,p3,(0,0,0),4)

points=np.array([[110,200],[330,200],[290,220],[220,250]],np.int32) #köşe koordinatlarını bir dizide tuttuk ve dizideki değerlerin tipini belirtmek zorundayız
cv2.polylines(canvas,[points], True,(0,0,100),5)#düzgün olmayan ve farklı kenar sayılarına sahip şekiller için kullanılacak #true kapalı bir şekil #renk,kalınlık

cv2.ellipse(canvas,(300,300),(80,20),10,90,360,(255,255,0),-1)#elips fonksiyonu#merkez,genişlik,yükseklik,yatayaçı,başlangıçaçı,bitişaçı,renk,kalınlık

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()