import cv2
import numpy as np
from yolo_model import YOLO

yolo = YOLO(0.6, 0.5) 
file = "data/coco_classes.txt" #yolodaki sınıflar

with open(file) as f:
    class_name = f.readlines()

#isimlerdeki boşlukları silme     
all_classes = [c.strip() for c in class_name]

#tespit edilecek resim
path = r"C:\Users\seyma\Desktop\media\dog_cat.jpg"
image = cv2.imread(path)
cv2.imshow("image",image)

#yolo ya uygun resim düzenleme
pimage = cv2.resize(image, (416,416))
pimage = np.array(pimage, dtype = "float32")
pimage /= 255.0 #normalizasyon
pimage = np.expand_dims(pimage, axis = 0) #genişletme

# yolo
boxes, classes, scores = yolo.predict(pimage, image.shape)

#görselleştirme
for box, score, cl in zip(boxes, scores, classes):
    
    x,y,w,h = box
    
    top = max(0, np.floor(x + 0.5).astype(int))
    left = max(0, np.floor(y + 0.5).astype(int))
    right = max(0, np.floor(x + w + 0.5).astype(int))
    bottom = max(0, np.floor(y + h + 0.5).astype(int))

    cv2.rectangle(image, (top,left), (right, bottom),(255,0,0),2)
    cv2.putText(image, "{} {}".format(all_classes[cl],score),(top,left-6),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1,cv2.LINE_AA)
    
cv2.imshow("yolo",image)    
cv2.waitKey(0)
cv2.destroyAllWindows()