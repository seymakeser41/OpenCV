import cv2
import numpy as np
#videoyu dahil etti
vid=cv2.VideoCapture("python_opencv_project/media/traffic.avi")
#arka planı videodan çekti
backsub=cv2.createBackgroundSubtractorMOG2()
#sayac ile arabaları sayacağız
c=0

while 1:
    ret,frame=vid.read()#frameleri çekti
    if ret:#eğer frameler düZgün çekildiyse işlem yapacak
        fgmask=backsub.apply(frame)#arka planı siyah yaptı
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)#iki çizgi çizdi ve arasında arac algılayacak
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)
        #Countourları buldu
        countours,hierarchy=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #hata oluşmaması için hierarchy değeri bulamazsa boş kalmasını sağladı
        try: hierarchy=hierarchy[0]
        except:hierarchy=[]
        
        for countor, hier in zip(countours,hierarchy):
            (x,y,w,h)=cv2.boundingRect(countor)
            if w>40 and h>40:#eğer bu değerlerden büyükse orada bir araç vardır
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:
                    c+=1
        #bulduğu arabalara isimle de gösterdi            
        cv2.putText(frame,"car"+ str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,255),2,cv2.LINE_AA)
        
        cv2.imshow("car counter",frame)
        cv2.imshow("fgmask",fgmask)
        
        if cv2.waitKey(20) & 0xFF == ord("q"):
            break
    
vid.release()
cv2.destroyAllWindows()
