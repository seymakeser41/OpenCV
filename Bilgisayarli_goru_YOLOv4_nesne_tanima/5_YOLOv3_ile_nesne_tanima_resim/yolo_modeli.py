#kütüphaneler
import cv2
import numpy as np 

img=cv2.imread(r"C:\Users\seyma\Desktop\media\people.png")

#print(img.shape)

img_width=img.shape[1]
img_height=img.shape[0]
#model için resmin 4 boyutlu tensor hali
img_blob=cv2.dnn.blobFromImage(img, 1/255, (416,416),swapRB=True, crop=False ) #boyutlandırma ölçüsü, boyutu, RGB , kırpma 
#print(img_blob.shape)

#sınıfları tanimlama
labels=["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
             "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
             "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
             "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
             "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
             "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
             "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
             "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
             "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
             "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]


#sınıflara farklı renkler 
colors=["0,255,255","0,0,255","255,0,0","255,255,0","0,255,0"]
#int'e çevirme 
colors=[np.array(color.split(",")).astype("int") for color in colors]
#dizi haline getirme
colors=np.array(colors)
#matrisi artırarak renkleri çoğaltma
colors=np.tile(colors,(18,1))


#modeli dahil etme (pjreddie yolo sitesinden indirilen cnf ve weight dosyası )
model=cv2.dnn.readNetFromDarknet("C:\Users\seyma\Desktop\media\yolo_model\yolov3.cfg","C:\Users\seyma\Desktop\media\yolo_model\yolov3.weights")
#tespit için katmanları çekme 
layers=model.getLayerNames()
#çıktı katmanlarını çekme 
#output_layer=[layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]
try:
    output_layer = [layers[i - 1] for i in model.getUnconnectedOutLayers()]
except:
    output_layer = [layers[i[0] - 1] for i in model.getUnconnectedOutLayers()]
#resmi gönderme 
model.setInput(img_blob)
#tespit işlemi yapılan katmanları çekme
detection_layers=model.forward(output_layer)

for detection_layer in detection_layers:
    for object_detection in detection_layer:

        #güven skoru tespit etme
        scores= object_detection[5:]
        predicted_id=np.argmax(scores)
        confidence= scores[predicted_id]

        #görselleştirme bounding box
        if confidence> 0.30:
            label=labels[predicted_id]
            bounding_box= object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
            (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
            
            start_x= int(box_center_x- (box_width/2))
            start_y= int(box_center_y- (box_height/2))

            end_x= start_x+ box_width
            end_y= start_y + box_height

            box_color=colors[predicted_id]
            box_color=[int(each) for each in box_color]

            label="{}: {:.2f}%".format(label, confidence*100)
            print("predicted object {}".format(label))

            cv2.rectangle(img, (start_x,start_y),(end_x,end_y), box_color, 1)
            cv2.putText(img, label, (start_x, start_y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)


cv2.imshow("detection ",img)
cv2.waitKey(0)
cv2.destroyAllWindows()