
import cv2
import numpy as np

vid=cv2.VideoCapture(r"media\line.mp4")

while True:
    ret,frame=vid.read()
    frame=cv2.resize(frame,(640,480))#daha güzel görüntüleyebilmek için boyutlandýrdýk
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #tek tek frameleri çekip hsv formata çevirdi
    
    lower_yellow=np.array([18,94,140],np.uint8)#hsv range for... #alt sarý deðerimizin hsv kodunu girerek belirttik
    upper_yellow=np.array([48,255,255],np.uint8)#üst sarý deðerimizin hsv kodunu girerek belirttik

    mask=cv2.inRange(hsv,lower_yellow,upper_yellow) #maskeledik

    edges=cv2.Canny(mask,75,250) #belirlediðimiz sarý çizgilerin köþelerini tespit ettik

    lines=cv2.HoughLinesP(edges,1,np.pi/180, 50,maxLineGap=50)#köþeleri kullanarak çizgileri çizdik

    for line in lines:#kenarlarý çizdi
        x1,y1,x2,y2=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)

    cv2.imshow("IMG", frame) 

    if cv2.waitKey(20)& 0xFF ==ord("q"):
    
        break
    
vid.release()
cv2.destroyAllWindows()
