import cv2
import numpy as np
import math #matematik işlemleri için kolaylık sağlayacak kütüphane

vid=cv2.VideoCapture(0)#görüntüyü kameradan aldık

while (1):
    try:
        ret,frame=vid.read()#frameleri çektik
        if not ret:
            print("Kamera verisi alinamiyor!")
            break


        frame=cv2.flip(frame,1)#y eksenine göre tersi alındı

        kernel=np.ones((3,3),np.uint8) #ilriki işlemler için kernel oluşturuduk

        roi=frame[100:300,100:300]#ilgileniceğimiz bölgeyi seçtik
        cv2.rectangle(frame,(100,100),(300,300),(0,0,255),0)#seçtiğimiz bölgeyi çizdik

        hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)#o bölgede tespit yapacağımız(mask işlemi için) için hsv formatına çevirdik

        lower_skin=np.array([0,20,70],dtype=np.uint8)#derimizi tespit edeceğinden deri rengimize göre alt ve üst değer belirledik
        upper_skin=np.array([20,255,255],dtype=np.uint8)#buğday ten için belirlenmiştir, bu değeri kendinize göre düzenleyin

        mask=cv2.inRange(hsv,lower_skin,upper_skin)#maskeledik
        mask=cv2.dilate(mask,kernel,iterations=4)#maskedelnmiş görüntüde bozuklaları beyazlaştırmak için 4 kere kerneli resme uyguladık
        mask=cv2.GaussianBlur(mask,(5,5),100) #gürültüleri azaltmak için blur yöntemi uygulandı
        
        contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#maskelediğimiz görüntüyü kullanarak konturlar oluşturduk
        cnt=max(contours,key=lambda x:cv2.contourArea(x))#alanları alınan konturlardan en büyüğünü döndürecek

        epsilon=0.0005*cv2.arcLength(cnt,True)#epsilon ve approx değerleri ile konturlara daha çok yaklaşırız
        approx=cv2.approxPolyDP(cnt,epsilon,True)

        hull=cv2.convexHull(cnt)#dışarıya dışbükey bir örtü oluşturduk

        areaHull=cv2.contourArea(hull)#hull bölgesinin alannı hesapladık
        areaHand=cv2.contourArea(cnt)#elimizin alanını hesapladık
        areaRatio=((areaHull-areaHand)/areaHand)*100  #boş alanın elimize oranını hesapladık

        hull=cv2.convexHull(approx, returnPoints=False) #konturların indislerine eriştik (false dediğimiz için indisleri döndürdü yoksa konturları döndürür)
        defects=cv2.convexityDefects(approx,hull) #konturlardaki kusurları bulduk

        l=0 #başlangıçta kusur değerini 0 olarak bir değişkende tuttuk

        for i in range(defects.shape[0]):#kusurlarda gezineceğiz
            s,e,f,d=defects[i,0]#her elemanın ilk indisi kullanıcak
            start=tuple(approx[s][0])#approx yaklaşımıyla değerleri çektik
            end=tuple(approx[e][0])
            far=tuple(approx[f][0])
            #bu noktaları kullanarak üçgenin kenarlarını bulduk
            a=math.sqrt((end[0]-start[0])**2+(end[1]-start[1])**2)
            b=math.sqrt((far[0]-start[0])**2+(far[1]-start[1])**2)
            c=math.sqrt((end[0]-far[0])**2+(end[1]-far[1])**2)

            s=(a+b+c)/2
            area= math.sqrt(s*(s-a)*(s-b)*(s-c))#kenar uzunluğu bilinen üçgenin alanı hesaplandı
            d=(2*area)/a #noktalar ve dışbükey örtü arasındaki farkı hesapladı

            angle=math.acos((b**2+c**2-a**2)/(2*b*c))*57 #iki kenar arası açıyı bulduk

            if angle<=90 and d>30 : #açı doksandan küçük ve d 30dan büyükse kusur vardır 
                l+=1
                cv2.circle(roi,far,3,[255,0,0],-1) #kusurlara daireler çizer

            cv2.line(roi,start,end,[255,0,0],2)

        l+=1

        font=cv2.FONT_HERSHEY_SIMPLEX

        if l==1:
            if areaHand <2000:#el kutuda değilse yapılacaklar
                cv2.putText(frame,"elinizi kutuya getirin", (0,50),font,1,(0,0,255),3,cv2.LINE_AA)
            else:
                if areaRatio<12:#el kutuda demektir(elimin bulunmadığı alan yüzde 12 den küçük)
                    cv2.putText(frame,"0", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)
                elif areaRatio< 17.5: 
                    cv2.putText(frame,"bol şans", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)
                else:# eğer 1 hata varsa alana göre 1 yazıcak
                    cv2.putText(frame,"1", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        elif l==2:#kusur 2 ise 2 yazacak
            cv2.putText(frame,"2", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        elif l==3: 
            if areaRatio<27:#kusur 3 ve el dışı alanın yüzdesi 27 den küçükse 
                cv2.putText(frame,"3", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)
            else:
                cv2.putText(frame,"sorun yok", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        elif l==4:
            cv2.putText(frame,"4", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        elif l==5:
            cv2.putText(frame,"5", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        elif l==6:
            cv2.putText(frame,"yeniden konumlandir", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        else:
            cv2.putText(frame,"yeniden konumlandir", (0,50),font,2,(0,0,255),3,cv2.LINE_AA)

        cv2.imshow("mask", mask)
        cv2.imshow("frame", frame)


    except:
        pass


    k=cv2.waitKey(5) & 0xFF #esc ya basınca çıkar
    if k==27:
        break


vid.release()
cv2.destroyAllWindows()
