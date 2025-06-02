import cv2 
import numpy as np
import matplotlib.pyplot as plt

bos=np.zeros(shape=(512,512,3),dtype=np.uint8)#boş siyah ekran
#yazı yazdık
cv2.putText(bos,text="merhaba",org=(10,500),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2,color=(255,255,255),thickness=3,lineType=2)

text=bos.copy()#koplayaladık

noktalar = np.array([[100, 300], [200, 200], [400, 300], [200, 400]], np.int32)
noktalar = noktalar.reshape((-1, 1, 2))  # OpenCV formatına sok
#4 nokta kullanarak kapalı şekil oluşturduk
cv2.polylines(text,[noktalar],isClosed=True, color=(255,0,0),thickness=5)

#görüntüleme
cv2.imshow('bos',bos)
cv2.imshow('poligon',text)

cv2.waitKey(0)
cv2.destroyAllWindows()