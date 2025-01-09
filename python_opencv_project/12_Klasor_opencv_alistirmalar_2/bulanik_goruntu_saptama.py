import cv2
import numpy as np

img=cv2.imread(r"python_opencv_project/media/starwars.jpg")
blur_img=cv2.medianBlur(img,7)#resmi blur işlemi ile bozduk

laplacian=cv2.Laplacian(blur_img,cv2.CV_64F).var()#bu fonksiyon ne kadar bozuk olduğunu anlamamıza yarar. bozuldukça resim gönderdiği değer küçülür

if laplacian<500:#belli bir değer altındaysa blurlu diyebiliriz
    print("blurlu resim")
    
else:
    print("blursuz resim")

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()