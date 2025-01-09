import cv2

img=cv2.imread(r"media/kus_resmi.jpg")

dimension=img.shape #imgin kaça kaçlık olduğuu verir
print(dimension)

color=img[150,200]#herhangi bir koordinattaki renk değerlerine ılaştık
print(color)

blue=img[420,500,0] #mavi BGR sıkalasında birinci olduğu için 0 girilir
print(blue)#420 ye 500 deki blue değerini verir

img[420,500,0]=250 #yeni blue değerimiz
print("new blue:" ,img[420,500,0])

blue1=img.item(150,200,0)#item fonksiyonu ile de pikseldeki BGR değerine ulaşabiliriz
print("blue1:",blue1)
img.itemset((150,200,0),172)# itemset ile belirttiğimiz piksel değerini değiştirebiliriz
print("new blue1:",img[150,200,0])#buraya blue1 yazılmaz çünkü biz pikselin değerini değiştirdik blue1i değil


cv2.imshow("resim " ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
