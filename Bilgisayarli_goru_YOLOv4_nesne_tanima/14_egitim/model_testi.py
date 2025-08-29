
#kütüphaneler
import cv2
import numpy as np 

cap=cv2.VideoCapture(r"C:\Users\seyma\Desktop\media\spot_baston_dynamic.mp4" )

while True:
    ret,frame=cap.read()

    img_width=frame.shape[1]
    img_height=frame.shape[0]
    #model için resmin 4 boyutlu tensor hali
    img_blob=cv2.dnn.blobFromImage(frame, 1/255, (416,416),swapRB=True, crop=False ) #boyutlandırma ölçüsü, boyutu, RGB , kırpma 
    #print(img_blob.shape)

    #sınıfları tanimlama
    labels=["spot"]

    #sınıflara farklı renkler 
    colors=["0,255,255"]
    #int'e çevirme 
    colors=[np.array(color.split(",")).astype("int") for color in colors]
    #dizi haline getirme
    colors=np.array(colors)
    #matrisi artırarak renkleri çoğaltma
    colors=np.tile(colors,(18,1))

    #modeli dahil etme (pjreddie yolo sitesinden indirilen cnf ve weight dosyası )
    model=cv2.dnn.readNetFromDarknet(r"C:\Users\seyma\Desktop\media\spot\spot_yolov4.cfg",r"C:\Users\seyma\Desktop\media\spot\spot_yolov4_final.weights")
    #tespit için katmanları çekme 
    #layers=model.getLayerNames()
    #çıktı katmanlarını çekme 
    #output_layer=[layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]

    layers = model.getLayerNames()
    output_layer = [layers[i - 1] for i in model.getUnconnectedOutLayers()]
    #resmi gönderme 
    model.setInput(img_blob)
    #tespit işlemi yapılan katmanları çekme
    detection_layers=model.forward(output_layer)
    
    #NON MAXIMUM SUPPRESSION adim 1 değişken listeleri
    ids_list=[]
    boxes_list=[]
    confidences_list=[]



    for detection_layer in detection_layers:
        for object_detection in detection_layer:

            #güven skoru tespit etme
            scores= object_detection[5:]
        
            predicted_id=np.argmax(scores)
            confidence= scores[predicted_id]

            #görselleştirme bounding box
            if confidence> 0.30:
                if predicted_id < len(labels):
                    label = labels[predicted_id]
                else:
                    label = "Spot | Boston Dynamics"
                #label=labels[predicted_id]
                bounding_box= object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
                (box_center_x, box_center_y, box_width, box_height) = bounding_box.astype("int")
                
                start_x= int(box_center_x- (box_width/2))
                start_y= int(box_center_y- (box_height/2))

                #non maximum suppression listelerini doldurma adim2 kutuları tutma 
                ids_list.append(predicted_id)
                confidences_list.append(float(confidence))
                boxes_list.append([start_x, start_y, int(box_width), int(box_height)])
                

    #non maximum suppression adim 3 
    #max güvenilirliğe sahip idleri alma
    max_ids=cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5,0.4)
    for max_id in max_ids:
        #max_class_id=max_id[0]
        max_class_id = int(max_id)
        box=boxes_list[max_class_id]

        start_x=box[0]
        start_y=box[1]
        box_width=box[2]
        box_height=box[3]

        predicted_id=ids_list[max_class_id]
        #label=labels[predicted_id]
        if predicted_id < len(labels):
            label = labels[predicted_id]
        else:
            # Modelin yanlış bir ID döndürdüğü durumlarda varsayılan etiket
            label = "Spot"
        confidence=confidences_list[max_class_id]




        end_x= start_x+ box_width
        end_y= start_y + box_height

        box_color=colors[predicted_id]
        box_color=[int(each) for each in box_color]

        label="{}: {:.2f}%".format(label, confidence*100)
        print("predicted object {}".format(label))

        cv2.rectangle(frame, (start_x,start_y),(end_x,end_y), box_color, 1)
        
        cv2.putText(frame, label, (start_x, start_y -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 3)


    cv2.imshow("detection ",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

