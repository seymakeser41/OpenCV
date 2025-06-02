#ARABA PLAKASI TANIMA PROJESİ


import cv2
import numpy as np
import matplotlib.pyplot as plt

plaka=cv2.imread(r"C:\Users\seyma\Desktop\media\car_plaka.png")

#haarcascade_russian_plate_number.xml isimli HaarCascade xml dosyasını yükleyiniz
cascade=cv2.CascadeClassifier(r"C:\Users\seyma\Desktop\opencv_bolumu\cascade\haarcascade_russian_plate_number.xml")

# detect_plate isimli tespit eden ve dikdörtgen çizen bir fonksiyon oluştur
def detect_plate(img):
    plate_img=img.copy()
    plate_recs=cascade.detectMultiScale(plate_img, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))
    for(x,y,w,h) in plate_recs:
        cv2.rectangle(plate_img, (x,y), (x+w, y+h),(255,0,0),6)

    return plate_img


#detect_and_blur_plate adında başka bir fonksiyonla blur işlemiyle plakanın görünmesini engelle

def detect_and_blur_plate(img):
    plate_img=img.copy()
    roi=img.copy()
    plate_recs=cascade.detectMultiScale(plate_img, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))
    if len(plate_recs) == 0:
        print("Plaka bulunamadi.")
    else:
        for(x,y,w,h) in plate_recs:
            roi=roi[y:y+h, x:x+w]
            blur_roi=cv2.medianBlur(roi,7)
            plate_img[y:y+h, x:x+w] = blur_roi

    return plate_img


result1=detect_plate(plaka)
result2=detect_and_blur_plate(plaka)
cv2.imshow('araba', plaka)
cv2.imshow('tespit', result1)
cv2.imshow('tespit_blur', result2)
cv2.waitKey(0)
cv2.destroyAllWindows()

