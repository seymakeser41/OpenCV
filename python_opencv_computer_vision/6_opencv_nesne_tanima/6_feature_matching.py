import cv2
import numpy as np
import matplotlib.pyplot as plt

urun=cv2.imread(r"C:\Users\seyma\Desktop\media\gevrek.webp")
raf=cv2.imread(r"C:\Users\seyma\Desktop\media\raf.png")
gray1=cv2.cvtColor(urun, cv2.COLOR_RGB2GRAY)
gray2=cv2.cvtColor(raf, cv2.COLOR_RGB2GRAY)

#Brute Force Detection with ORB Description methodu
#obje oluşturur
orb = cv2.ORB_create()
#objenin keypointleri ve destcriptorlarını belirle 
kp1, dest1= orb.detectAndCompute(urun,None)
kp2, dest2= orb.detectAndCompute(raf,None)
#eşlenikleri belirle
bf=cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# obje için eşleşme oluşturur
matches= bf.match(dest1, dest2)
#uzaklıklarına göre sıralama yapılır
matches= sorted(matches, key=lambda x:x.distance) 
#ilk 25 eşleşmeyi çizdirme işlemi
cizdirme= cv2.drawMatches(urun, kp1, raf,kp2, matches[:25],None, flags=2)

#Burce Force Matching ile SIFT Descriptors ve Ratio Test 
#obje oluştur 
sift=cv2.xfeatures2d.SIFT_create()
#objenin keypointleri ve destcriptorlarını belirle 
kp3, dest3= sift.detectAndCompute(urun,None)
kp4, dest4= sift.detectAndCompute(raf,None)
#eşleşmeleri belirle
bf2= cv2.BFMatcher()
matches2=bf2.knnMatch(dest3, dest4, k=2)
#eşleniklerin en iyilerini bulmak için 2li sıralamada ikisini karşılaştırıp en yakınını aldı
good=[]
for match1, match2 in matches2:
    if match1.distance < 0.75* match2.distance:
        good.append([match1])


cizdirme2= cv2.drawMatchesKnn(urun, kp3,raf,kp4, good, None, flags=2)


#FLANN based Matcher methodu

#obje oluştur
sift2=cv2.xfeatures2d.SIFT_create()
#objenin keypointleri ve destcriptorlarını belirle 
kp5, dest5= sift2.detectAndCompute(urun,None)
kp6, dest6= sift2.detectAndCompute(raf,None)
#matcher fonksyonu için gerekli default değişkenler 
FLANN_INDEX_KDTREE=0
index_params=dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params=dict(checks=50)

#eşleşmeleri belirle
fb=cv2.FlannBasedMatcher(index_params, search_params)
matches3=fb.knnMatch(dest5, dest6, k=2)
#eşleniklerin en iyilerini bulmak için 2li sıralamada ikisini karşılaştırıp en yakınını aldı
good1=[]
for match1, match2 in matches3:
    if match1.distance < 0.75* match2.distance:
        good1.append([match1])


cizdirme3= cv2.drawMatchesKnn(urun, kp5,raf,kp6, good1, None, flags=2)

#istediğimiz eşleşmelrin renklerini değiştirdik 
good2 = []
matchesMask = []

for m in matches3:
    if len(m) == 2:  # KNN sonucu 2 eşleşme varsa değerlendir
        match1, match2 = m
        if match1.distance < 0.75 * match2.distance:
            good2.append([match1])
            matchesMask.append([1, 0])  # sadece ilk eşleşmeyi çiz

cizdirme4 = cv2.drawMatchesKnn(urun, kp5, raf, kp6, good2, None,
                               matchesMask=matchesMask,
                               matchColor=(0,0, 255),
                               singlePointColor=(255, 0, 0),
                               flags=0)


cv2.imshow('gevrek', urun)
cv2.imshow('raf', raf)
cv2.imshow('gri1', gray1)
cv2.imshow('gri2', gray2)
cv2.imshow('cizme', cizdirme)
cv2.imshow('cizme_2', cizdirme2)
cv2.imshow('cizme_3', cizdirme3)
cv2.imshow('cizme_4', cizdirme4)
cv2.waitKey(0)
cv2.destroyAllWindows()