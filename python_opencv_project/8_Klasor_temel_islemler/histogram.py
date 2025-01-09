import cv2
import numpy as np
from matplotlib import pyplot as plt

img=np.zeros((500,500),np.uint8)+100#histogramlar için kendimiz resim oluşturacağız 500 e 500lük bir siyah ekran oluşturduk 100 ekleyerek renklendirdik
cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)#ekrana resimler çiziyoruz
cv2.rectangle(img,(200,170),(350,200),(255,255,255),-1)
img1=cv2.imread(r"C:\Users\SEYMAKESER\PycharmProjects\python_opencv_project\media\smile.jpg")
b,g,r=cv2.split(img1)#bgr değerlerini görüntüledik

cv2.imshow("img",img)
plt.hist(img.ravel(),256,[0,256])#histogramı çizdik #ilk parametre tek satır haline getirir ikinci değer sayısısnı üçüncü değer aralığını verir
plt.show()#histogrami gösterdik

cv2.imshow("img1",img1)
plt.hist(img1.ravel(),256,[0,256])#histogramı çizdik #ilk parametre tek satır haline getirir ikinci değer sayısısnı üçüncü değer aralığını verir
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()#histogrami gösterdik

cv2.waitKey(0)
cv2.destroyAllWindows()



