import cv2
import numpy as np
import matplotlib.pyplot as plt
#görseller yüklendi
erkek=cv2.imread(r"C:\Users\seyma\Desktop\media\erkek.png")
kadin=cv2.imread(r"C:\Users\seyma\Desktop\media\kadin.png")
toplu=cv2.imread(r"C:\Users\seyma\Desktop\media\toplu.png")
gray_1=cv2.cvtColor(erkek,cv2.COLOR_RGB2GRAY) #gri format
#yüz tespiti içi kullanılacak cascade
face_cascade=cv2.CascadeClassifier(r"C:\Users\seyma\Desktop\opencv_bolumu\cascade\frontalface.xml.xml")
#göz tespiti için kullanılacak cascade
eye_cascade=cv2.CascadeClassifier(r"C:\Users\seyma\Desktop\opencv_bolumu\cascade\haarcascade_eye.xml")

#resim üzerinde cascade ile yüz bulunur ve koordinatlar döndürürlür, bunları kullanarak dikdörtgen çizerek görselleştirdik
def detect_face(img):
    face_img=img.copy()
    face_recs=face_cascade.detectMultiScale(face_img)
    for(x,y,w,h) in face_recs:
        cv2.rectangle(face_img, (x,y), (x+w, y+h),(255,255,255),10)

    return face_img

#resim üzerinde cascade ilegözler bulunur ve koordinatlar döndürürlür, bunları kullanarak dikdörtgen çizerek görselleştirdik
def detect_eye(img):
    eye_img=img.copy()
    eye_recs=eye_cascade.detectMultiScale(eye_img)
    for(x,y,w,h) in eye_recs:
        cv2.rectangle(eye_img, (x,y), (x+w, y+h),(255,0,0),5)
    return eye_img
#resimleri fonksiyona göndererek sonuçları çıkardık
result=detect_face(erkek)
result1=detect_face(kadin)
result2=detect_face(toplu)

result3=detect_eye(erkek)
result4=detect_eye(kadin)#çok istenen sonuç değildir
result5=detect_eye(toplu)#çok istenen sonuç değildir

#görselleştirme
cv2.imshow('erkek',erkek)
cv2.imshow('kadin',kadin)
cv2.imshow('toplu',toplu)
cv2.imshow('tespit_erkek', result)
cv2.imshow('tespit_kadin', result1)
cv2.imshow('tespit_toplu', result2)
cv2.imshow('tespit_erkek_goz', result3)
cv2.imshow('tespit_kadin_goz', result4)
cv2.imshow('tespit_toplu_goz', result5)
cv2.waitKey(0)
cv2.destroyAllWindows()
