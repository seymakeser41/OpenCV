
import cv2
import numpy as np

vid=cv2.VideoCapture(r"media\line.mp4")

while True:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,480))#daha g�zel g�r�nt�leyebilmek i�in boyutland�rd�k
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #tek tek frameleri �ekip hsv formata �evirdi
    
    lower_yellow=np.array([18,94,140],np.uint8)#hsv range for... #alt sar� de�erimizin hsv kodunu girerek belirttik
    upper_yellow=np.array([48,255,255],np.uint8)#�st sar� de�erimizin hsv kodunu girerek belirttik

    mask=cv2.inRange(hsv,lower_yellow,upper_yellow) #maskeledik

    edges=cv2.Canny(mask,75,250) #belirledi�imiz sar� �izgilerin k��elerini tespit ettik

    lines=cv2.HoughLinesP(edges,1,np.pi/180, 50,maxLineGap=50)#k��eleri kullanarak �izgileri �izdik

    for line in lines:#kenarlar� �izdi
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("IMG", frame) 

    if cv2.waitKey(20)& 0xFF ==ord("q"):
    
        break
    
vid.release()
cv2.destroyAllWindows()
