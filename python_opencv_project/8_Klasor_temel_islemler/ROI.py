# ROİ=region of interest= ilgi alanı
import cv2
img=cv2.imread(r"media/kus_resmi.jpg")

print(img.shape[:2])#resmimizin piksel boyutunu aldık

roi=img[0:400,800:1400]#tahmini olarak resimdeki bir bölgeyi aldık

cv2.imshow("resim",img)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()