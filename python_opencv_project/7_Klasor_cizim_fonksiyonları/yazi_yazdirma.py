import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) +255

font1=cv2.FONT_HERSHEY_SIMPLEX
font2=cv2.FONT_HERSHEY_COMPLEX
font3=cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(canvas,"opencv",(50,100),font1,2,(0,0,0),cv2.LINE_AA) #yazı yazma fonksiyonu ekran,yazımız,başlangıç ,fonttipi,boyut,renk,varsayılan tip
cv2.putText(canvas,"opencv",(50,200),font2,2,(0,0,0),cv2.LINE_AA)
cv2.putText(canvas,"opencv",(50,300),font3,2,(0,0,0),cv2.LINE_AA)

cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()