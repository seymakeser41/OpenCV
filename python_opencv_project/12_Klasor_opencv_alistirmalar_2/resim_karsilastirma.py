import cv2
import numpy as np

path1="media/aircraft.jpg"
path2="media/aircraft_1.jpg"
img1=cv2.imread(path1)
img1=cv2.resize(img1,(640,550))
img2=cv2.imread(path2)
img2=cv2.resize(img2,(640,550))#iki resmin pikselleri eşit olmazsa aynı resim bile olsa eşit olsa
img3=cv2.medianBlur(img1,7)#blur işlemiyle resmi bozdu
if img1.shape==img2.shape:#iki resmin eşitliğini değerlendirebilmek için önce boyutlarını karşılaştırdık
    print("same size(img1 and img2)")
else:
    print("not same(img1 and img2)")
    
diff=cv2.subtract(img1,img2)#resimleri karşılaştırıp farklılıkları ortaya çıkarır, farklı yerleri beyaz, aynı yerleri siyah yapar
b,g,r=cv2.split(diff)#herhangi bir renk içeriyor mu diye b,g,r değerlerini kontrol edecek

if cv2.countNonZero(b)==0 and cv2.countNonZero(g) and cv2.countNonZero(r):#eğer 0 değilse yani 0 dan farklı değerleri tutar
    print("completely equal(img1 and img2)")#tamamen eşit
else:
    print("not completely equal(img1 and img2) ")
    
    
    
if img3.shape==img2.shape:#iki resmin eşitliğini değerlendirebilmek için önce boyutlarını karşılaştırdık
    print("same size(img3 and img2)")
else:
    print("not same(img3 and img2)")
    
diff_2=cv2.subtract(img3,img2)#resimleri karşılaştırıp farklılıkları ortaya çıkarır, farklı yerleri beyaz, aynı yerleri siyah yapar
b_2,g_2,r_2=cv2.split(diff_2)#herhangi bir renk içeriyor mu diye b,g,r değerlerini kontrol edecek

if cv2.countNonZero(b_2)==0 and cv2.countNonZero(g_2) and cv2.countNonZero(r_2):#eğer 0 değilse yani 0 dan farklı değerleri tutar
    print("completely equal(img3 and img2)")#tamamen eşit
else:
    print("not completely equal (img3 and img2)")
    


cv2.imshow("aircraft",img1)
cv2.imshow("aircraft_1",img2)
cv2.imshow("aircraft_blur",img3)
cv2.imshow("differance",diff)
cv2.imshow("differance_2",diff_2)
cv2.waitKey(0)
cv2.destroyAllWindows()