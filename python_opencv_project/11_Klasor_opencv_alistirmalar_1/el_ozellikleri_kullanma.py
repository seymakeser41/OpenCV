import cv2
import numpy as np
import math
#yüzdeki en uç noktaları bulup aradaki açıyı bulduk

def findMaxContours(contours):#max alanı bulmak için fonksiyon
    max_i=0
    max_area=0
    
    for i in range(len(contours)):
        area_hand=cv2.contourArea(contours[i])#bütün contourların alanını bulucak
        if max_area<area_hand:
            max_area=area_hand
            max_i=i
            
        try:#eğer bir contour alanı bulunamazsa hata vermesin diye try except bloğu gerekli
            c=contours[max_i]
        except:
            contours=[0]
            c=contours[0]
            
        return c
    
cap=cv2.VideoCapture(0)

while 1:
    ret,frame=cap.read()
    frame= cv2.flip(frame,1)
    roi= frame[50:250,250:450]# framelerin y1:y2, x1:x2 #bu bölümü kesip gösterir
    
    cv2.rectangle(frame,(250,50),(450,250),(0,0,255),0)#x1,y1 ve x2,y2 ye dikdörtgen çizer, yüzü çevrelemek için
    #eğer kalınlık verilirse hsvye dahil olur hata verir
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)#roi ile seçtiğimiz nesneyi tanımlamak için hsv formatına çevirdi
    lower_color= np.array([0,45,79])#renk aralığını belirledik
    upper_color=np.array([17,255,255])
    
    mask=cv2.inRange(hsv,lower_color,upper_color)#maskeledik siyah beyaz
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1)#görüntüdeki bulanıklık azalır
    mask=cv2.medianBlur(mask,15)#bulanıklık daha da azalır
    
    contours,_=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#Maskelenmiş resime contour yaptık
    
    if len(contours)>0:#eğer contour 0 dan küçükse yani küçük siyahlıklarsa
        
            c=findMaxContours(contours)
            
            extLeft=tuple(c[c[:,:,0].argmin()][0])#en küçük x leri bulacak
            extRight=tuple(c[c[:,:,0].argmax()][0])#sağda olduğu için büyük xi bulacak
            extTop=tuple(c[c[:,:,1].argmin()][0])# y olduğu için 1 dedik ve ynin min değerini bulacak
            
            
            cv2.circle(roi,extLeft,5,(0,255,0),2)#noktalara çember çizdik
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            
            
            cv2.line(roi,extLeft,extTop,(255,255,0),2)#noktaları kullanarak çizgiler çizerek çokgen oluşturur
            cv2.line(roi,extTop,extRight,(255,255,0),2)
            cv2.line(roi,extRight,extLeft,(255,255,0),2)
            
            
            a=math.sqrt((extRight[0]-extTop[0])**2+ (extRight[1]-extTop[1])**2) #çokgendeki sağdaki iki kenar ve ar aköşegeni kullanarak açıyı buldu
            c=math.sqrt((extTop[0]-extLeft[0])**2+ (extTop[1]-extLeft[1])**2)
            b=math.sqrt((extRight[0]-extLeft[0])**2+ (extRight[1]-extLeft[1])**2)
            
            try:
                angle_ab=int(math.acos((a**2+b**2-c**2)/(2*b*c))*57) #açıyı hesapladı 0 olma ihtimaline karşı try except kullandı
                if angle_ab>70:#eğer acı 70den büyükse dikdörtgen çizer
                    cv2.rectangle(frame,(0,0),(100,100),(255,0,0),-1)
                else:
                    pass
                    
                cv2.putText(roi,str(angle_ab),(extRight[0]-100, extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            except:
                cv2.putText(roi,"?",(extRight[0]-100, extRight[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            
    
    cv2.imshow("frame",frame)
    cv2.imshow("roi",roi)
    cv2.imshow("mask",mask)
    
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()