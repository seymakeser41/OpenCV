import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread(r"C:\Users\seyma\Desktop\media\starwars.jpg")
img_face=cv2.imread(r"C:\Users\seyma\Desktop\media\starwars2.jpg")

w1,h1,c1=img_face.shape

my_method= eval('cv2.TM_CCOEFF') #string verilen fonksiyon işlev için kullanılır
res=cv2.matchTemplate(img, img_face, my_method) #yüz resminin ilk resimle kesiştiği ilk noktayı bulur 

#bir sürü method vardır sırasıyla uygulayalım
methods = ['TM_CCOEFF', 'TM_CCOEFF_NORMED', 'TM_CCORR', 'TM_CCORR_NORMED', 'TM_SQDIFF', 'TM_SQDIFF_NORMED']
 
 #tüm methodları deneyerek kesişim noktasını ısı haritasından bulup en boy hesaplayıp dikdörtgen çizdirerek görüntüledik
for meth in methods:
    img1=img.copy()
    img2=img_face.copy()
    method=eval(f"cv2.{meth}")
    res=cv2.matchTemplate(img1, img2, method)
    min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left= min_loc

    else:
        top_left=max_loc

    bottom_right=(top_left[0] + w1, top_left[1] + h1)
    cv2.rectangle(img1, top_left, bottom_right, (255,0,0),5)

    plt.subplot(121)
    plt.imshow(res)
    plt.title('teplate matching')

    plt.subplot(122)
    plt.imshow(img1)
    plt.title('detection')

    plt.suptitle('m')
    plt.show()
    print('\n')
    





cv2.imshow('starwar', img)
cv2.imshow('starwar_face', img_face)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()