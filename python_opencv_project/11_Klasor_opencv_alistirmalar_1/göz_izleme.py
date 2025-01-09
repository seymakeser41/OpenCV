#göz çevresini bir roi ye alıp sonra göz merceğine bir dikdörtgen çizerek bu dikdörtgen üzerinden takip yapılacak
import cv2

vid=cv2.VideoCapture(r"media/eye_motion.mp4") 

while 1:
    ret,frame=vid.read()
    if ret is False:
        break
    
    roi=frame[80:210,230:450]#bölgeyi çektik
    rows,cols,_=roi.shape#boyutları tuttuk
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,thresold=cv2.threshold(gray,3,255,cv2.THRESH_BINARY_INV)#gözün siyah yerini beyaz yapıp merceği takip etmeye yarıcak
    
    contours,_=cv2.findContours(thresold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#contourları bulduk
    contours= sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)# contours değerlerini belirlenen fonksiyona göre sıralar(reverse true olduğundan ters sıralar)
    
    for cnt in contours:
       (x,y,w,h)=cv2.boundingRect(cnt)#dikdörtgenin koordinat değerlerini bu fonksiyonla çekti
       cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)#dikdörtgeni çizdi
       cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)#ana kenar ortayları çizer ve orta noktayı takip eder
       cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
       break
   
    frame[80:210,230:450]=roi #en son bölgeiy toplam framede görmek için roiyi frame atadık
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(80) & 0xFF == ord("q"):
        break
    
vid.release()
cv2.destroyAllWindows()
        