import cv2
import numpy as np

img_path = ("media/kus_resmi.jpg")
img = cv2.imread(img_path)

if img is None:
    print("Resim yüklenemedi. Dosya yolunu kontrol edin:", img_path)
else:
    print("Resim başarıyla yüklendi.")


#img=cv2.imread(r"C:\Users\ŞEYMA KESER\PycharmProjects\python_opencv_project\media\kus_resmi.jpg")
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)#Resmi 3 farklı renk uzayına dönüştürüp görüntüledik
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("resim",img)
cv2.imshow("resim1",img_rgb)
cv2.imshow("resim2",img_hsv)
cv2.imshow("resim3",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()