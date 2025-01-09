import cv2
import numpy as np

img=cv2.imread(r"python_opencv_project/media/bozuk_para.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.equalizeHist(gray)#histogram eşitleme ile kontrastı arttır

img_blur=cv2.medianBlur(gray,7)#resimdeki görültüyü azaltir


circles= cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,0.1,img.shape[0]/6, param1=100, param2=20, minRadius=25,maxRadius=60 )#resmi, yontemi, cemberler arasi mesafeyi belirten ifadeyi, fonksiyona tanimli gradient degeri ve threshold degeri , min ve max yaricap ile cemberleri belirledi

if circles is not None:
    circles=np.uint16(np.around(circles))#belirlenen cemberleri cizdi
    count = 0
    for i in circles[0,:]:
        count +=1
        cv2.circle(img,(i[0],i[1]),i[2], (0,255,0),2)
    
    cv2.putText(img,f"Count: {count}",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2,cv2.LINE_AA,)


cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()