"""
algoritma
1-gri format
2-kenarlari yumuşat
3-köşeleri tespit et
4-contourlari bul
5-maskeyle plakayi kirp
6-pytesseract ile plakayi oku
    """
#kütüphaneleri import ettik   
import cv2
import numpy as np
import pytesseract
import imutils
#resmi dahil ettik
img=cv2.imread("python_opencv_project/media/licence_plate.jpg")
#gri tona çevir
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#filtreledi, filtrelenmezse köşeler ayrıntılar fazla olur
filtered=cv2.bilateralFilter(gray,6,250,250)#çap,ve sigma değerleri
#köşelri algıladı
edged=cv2.Canny(filtered,30,200)
#contourları buldu
contours=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#imutils kullanarak contourları yakaldı
cnts=imutils.grab_contours(contours)
#koordinatları alanlarına göre tersten sıraladı
cnts=sorted(cnts,key=cv2.contourArea ,reverse=True)[:10]
#değer bulamamasına karşı none atadı
screen=None

for c in cnts:
    epsilon=0.018*cv2.arcLength(c,True)#deneysel bir katsayı kullanacak
    approx=cv2.approxPolyDP(c,epsilon,True)#counturlara daha çok yaklaştı
    if len(approx)==4:#4 köşe bulduysa dikdörtgen demektir bu da plakayı temsil eder
        screen=approx
        break
#maske kullandı
mask=np.zeros(gray.shape,np.uint8 )#plaka dışı her yeri siyah yapmak için kullanıldı
#plaka bölgesini beyaz yaparak ayırdı
new_img=cv2.drawContours(mask,[screen],0,(255,255,255),-1)
#plaka alanına yazıyı yapıştıracak
new_img=cv2.bitwise_and(img,img,mask=mask)
#resmi kırptı, beyaz koordinatları tuttu
(x,y)=np.where(mask==255)
#en üst x ve y koordinatları tuttu
(topx,topy)=(np.min(x),np.min(y))
#en alt koordinatları tuttu
(bottomx,bottomy)=(np.max(x),np.max(y))
#kırpılmış değeri tuttu
cropped=gray[topx:bottomx+1, topy:bottomy+1]
#yazıyı okudu
text=pytesseract.image_to_string(cropped,lang="eng")

cv2.imshow("1_licanse palette",img)
cv2.imshow("2_licanse palette_gray",gray)
cv2.imshow("3_licanse palette_filtered",filtered)
cv2.imshow("4_licanse palette_edged",edged)
cv2.imshow("mask",new_img)
cv2.imshow("cropped",cropped)
print("detected text:", text)
cv2.waitKey(0)
cv2.destroyAllWindows()


