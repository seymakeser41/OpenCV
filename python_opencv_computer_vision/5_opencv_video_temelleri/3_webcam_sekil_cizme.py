import cv2
#ilk kodda çektiğimiz videonun boyutlarının oranıyla elde ettiğimiz konumları kullanarak dikdortgen çizdik
#ikinci kodda ise ilk dokunduğumuz noktaya bir daire çizip sonra ikinci noktaya dokununca dikdörtgen çizen bir uygulama yaptık
"""
cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #boyutlari hesapladi
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x=width //2 #boyutlarin oranlariyla başlangic noktasi ve en, boy olusturdu
y=height //2
w= width//4
h=height//4

#her frame üzerindeki döngüyle dikdörtgen cizdi
while True:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
    cv2.imshow('frame',frame)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

"""
#bu fonksiyon click olaylarına göre gereken işlemleri yapacak
#sol tuşa basıldıysa o noktanın koordinatları alır ve sonra sıfırlanır
def ciz_dikdortgen(event,x,y,flag,param):
    global pt1,pt2,top_left_clicked,top_right_clicked

    if event== cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked==True & top_right_clicked==True:

            pt1=(0,0) 
            pt2=(0,0) 
            top_left_clicked= False 
            top_right_clicked=False

        if top_left_clicked==False:
            pt1=(x,y)
            top_left_clicked=True

        elif top_right_clicked==False:
            pt2=(x,y)
            top_right_clicked=True

    
pt1=(0,0) #fare olayından gelen ilk konum için default değişken 
pt2=(0,0) #fare olayından gelen ikinci konum için default değişken
top_left_clicked= False #fare olaylarını tutmak için default değişkenler
top_right_clicked=False

cap=cv2.VideoCapture(0)
cv2.namedWindow('test')
# fare olaylarını bu fonksiyondan alıp kontrol ettiğimiz ciz_dikdortgen fonksiyonuna yollarız
cv2.setMouseCallback('test', ciz_dikdortgen)

#click olaylarına göre şekilleri çizdik 
while True:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)
    
    if top_left_clicked==True:
        cv2.circle(frame,pt1,5,(0,0,255),-1 )

    if top_left_clicked and top_right_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255),4)

    cv2.imshow('test',frame)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
