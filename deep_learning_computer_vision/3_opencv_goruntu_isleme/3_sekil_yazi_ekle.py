import cv2
import numpy as np

#sekil ve yazı yazmak için yeni pencere 
img1=np.zeros((512,512,3), np.uint8)
cv2.imshow("siyah", img1)

#çizgi 
cv2.line(img1, (0,0),(512,512),(0,255,0))
cv2.imshow("cizgi", img1)

#dikdörtgen
cv2.rectangle(img1,(0,0),(256,256),(255,0,0), cv2.FILLED)
cv2.imshow("dikdörtgen", img1)

#çember
cv2.circle(img1,(300,300),45,(0,0,255), cv2.FILLED)
cv2.imshow("cember", img1)

#yazı
cv2.putText(img1,"resim",(350,350),cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255) )
cv2.imshow("metin", img1)


cv2.waitKey(0)
cv2.destroyAllWindows()