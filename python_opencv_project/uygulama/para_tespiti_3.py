import cv2
import numpy as np

img=cv2.imread(r"C:\Users\seyma\Desktop\media\para_3.jpg")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.equalizeHist(gray)#histogram eşitleme ile kontrastı arttır

img_blur=cv2.medianBlur(gray,11)#resimdeki görültüyü azaltir


circles= cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT,1.8,img.shape[0]/6, param1=200, param2=40, minRadius=100,maxRadius=250 )#resmi, yontemi, cemberler arasi mesafeyi belirten ifadeyi, fonksiyona tanimli gradient degeri ve threshold degeri , min ve max yaricap ile cemberleri belirledi

if circles is not None:
    circles=np.uint16(np.around(circles))#belirlenen cemberleri cizdi
    count = 0
    for i in circles[0,:]:
        count +=1
        cv2.circle(img,(i[0],i[1]),i[2], (0,255,0),2)
    
    cv2.putText(img,f"Count: {count}",(10, 30),cv2.FONT_HERSHEY_SIMPLEX,1,(0, 0, 255),2,cv2.LINE_AA,)

img=cv2.resize(img,(480,600))
img_blur=cv2.resize(img_blur,(480,600))
cv2.imshow("img",img)
cv2.imshow("blur",img_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()