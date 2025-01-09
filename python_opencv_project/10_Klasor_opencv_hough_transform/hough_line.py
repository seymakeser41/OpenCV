#doğrusal bir çizgidekiki her nokta a b düzleminde bir noktada kesişirler
import cv2
import numpy as np

img=cv2.imread(r"media/h_line.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray, 75,150) #köşeleri alt ve üst değer belirterek canny fonksiyonu ile bulduk
lines=cv2.HoughLinesP(edges,1,np.pi/180, 50) #köşeleri bulunmuş resimde kenarları tespit etti , ro , teta,ve trashold değerleri girdik
print(lines) # içerisinde 4 tane değer olan listeler bulundurur , bunlar kenarların bulunduğu yerler . dolayısıyla çizerken hepsini tek tek almamız gerekir
lines1=cv2.HoughLinesP(edges,1,np.pi/180, 50,maxLineGap=200)#boşlukları belirtilen değer kadar doldurur

for line in lines: #sadece kenarları çizmek için kullanılacak döngü
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) # başlangıç ve bitiş noktalarını kullanrak kenarları çizdi

"""
for line in lines1: #kenarları ve boşlukları çizen döngü
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2) # başlangıç ve bitiş noktalarını kullanrak kenarları çizdi
"""
cv2.imshow("original",img)
cv2.imshow("gray",gray)
cv2.imshow("edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()