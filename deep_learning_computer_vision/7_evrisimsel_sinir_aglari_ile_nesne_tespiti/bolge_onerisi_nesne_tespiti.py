"""
1-seçmeli arama
2-imagenet veri setiyle eğitilmiş resnet50 sinir aği"""


from tensorflow.keras.applications.resnet50 import preprocess_input 
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np
import cv2

from maksimum_olmayan_bastirma import non_max_suppression

#seçmeli arama algoritması (uzun sürmemesi için ilk 100 dikdörtgen dönecek)
def selective_search(image):
    print("ss")
    ss = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()
    ss.setBaseImage(image)
	
    ss.switchToSelectiveSearchQuality()
    
    rects = ss.process()
    
    return rects[:1000]


# model
model = ResNet50(weights="imagenet")    
image = cv2.imread(r"C:\Users\seyma\Desktop\media\animals.jpg") #hayvan resimleri bulunan resim
image = cv2.resize(image, dsize = (400,400))
(H, W) = image.shape[:2]


# seçmeli arama uygulaması
rects = selective_search(image)

#bölgeler belirlenip dizi olarak modele hazırlandı
proposals = []
boxes = []
for (x, y, w, h) in rects:

    #belli bir ölçünün altındaysa iterasyonu bir sonraki aşaöadan devam ettirme
    if w / float(W) < 0.1 or h / float(H) < 0.1: continue
    
    roi = image[y:y + h, x:x + w]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    roi = cv2.resize(roi, (224, 224))

    roi = img_to_array(roi)
    roi = preprocess_input(roi)

    proposals.append(roi)
    boxes.append((x, y, w, h))


proposals = np.array(proposals)

# model tahmini
print("predict")
preds = model.predict(proposals)
preds = imagenet_utils.decode_predictions(preds, top=1)

#çıkan sonuçlardan belli değer üzerinde olan kutucuklar alınacak
labels = {}
min_conf = 0.8
for (i, p) in enumerate(preds):
    
    
    (_, label, prob) = p[0]
    if prob >= min_conf:
        (x, y, w, h) = boxes[i]
        box = (x, y, x + w, y + h)
        L = labels.get(label, [])
        L.append((box, prob))
        labels[label] = L

#görselleşitme işlemi
clone = image.copy()
#kutucuklara maksimum olmayan bastırma uygulanır ve kutucuklar belirtilir
for label in labels.keys():
    for (box, prob) in labels[label]:
        boxes = np.array([p[0] for p in labels[label]])
        proba = np.array([p[1] for p in labels[label]])
        boxes = non_max_suppression(boxes, proba)
    
        for (startX, startY, endX, endY) in boxes:
            cv2.rectangle(clone, (startX, startY), (endX, endY),(0, 0, 255), 2)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.putText(clone, label, (startX, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
        cv2.imshow("After", clone)
        if cv2.waitKey(0) & 0xFF == ord('q'):break

cv2.destroyAllWindows()