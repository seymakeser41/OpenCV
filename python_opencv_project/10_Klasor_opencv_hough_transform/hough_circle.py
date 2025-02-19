
import cv2
import numpy as np

img1=cv2.imread(r"python_opencv_project/media/coins.jpg")
img2=cv2.imread(r"python_opencv_project/media/balls.jpg")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur=cv2.medianBlur(gray1,5)#resimdeki görültüyü azaltir
img2_blur=cv2.medianBlur(gray2,5)

circles1= cv2.HoughCircles(img1_blur, cv2.HOUGH_GRADIENT,1,img1.shape[0]/4, param1=200, param2=10, minRadius=15,maxRadius=80 )#resmi, yontemi, cemberler arasi mesafeyi belirten ifadeyi, fonksiyona tanimli gradient degeri ve threshold degeri , min ve max yaricap ile cemberleri belirledi
circles2= cv2.HoughCircles(img2_blur, cv2.HOUGH_GRADIENT,1,img2.shape[0]/4, param1=200, param2=10, minRadius=15,maxRadius=80 )

if circles1 is not None:
    circles1=np.uint16(np.around(circles1))#belirlenen cemberleri cizdi
    for i in circles1[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2], (0,255,0),2)

if circles2 is not None:
    circles2=np.uint16(np.around(circles2))
    for i in circles2[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2], (0,255,0),2)



cv2.imshow("img1",img1)
cv2.imshow("img2",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()