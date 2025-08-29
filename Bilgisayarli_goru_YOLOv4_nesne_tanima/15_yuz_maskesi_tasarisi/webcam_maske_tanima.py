import cv2
import numpy as np

# Webkamerayı başlat
cap = cv2.VideoCapture(0)

# Sınıflar
labels = ["good", "bad", "mask_incorrect"]

# Renkler
colors = ["0,255,255", "0,0,255", "0,255,0"]
colors = [np.array(c.split(",")).astype("int") for c in colors]
colors = np.array(colors)
colors = np.tile(colors, (18, 1))  # çoğaltma

# YOLO modelini yükle
model = cv2.dnn.readNetFromDarknet(
    r"C:\Users\seyma\Desktop\media\mask_detection\yolov3_mask.cfg",
    r"C:\Users\seyma\Desktop\media\mask_detection\yolov3_mask_last.weights"
)
layers = model.getLayerNames()
try:
    output_layer = [layers[i - 1] for i in model.getUnconnectedOutLayers()]
except:
    output_layer = [layers[i[0] - 1] for i in model.getUnconnectedOutLayers()]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_height, img_width = frame.shape[:2]

    # Resmi blob formatına çevir
    img_blob = cv2.dnn.blobFromImage(frame, 1/255, (416,416), swapRB=True, crop=False)

    model.setInput(img_blob)
    detection_layers = model.forward(output_layer)

    ids_list = []
    boxes_list = []
    confidences_list = []

    for detection_layer in detection_layers:
        for object_detection in detection_layer:
            scores = object_detection[5:]
            predicted_id = int(np.argmax(scores))
            confidence = scores[predicted_id]

            # Eğer sınıf labels içinde yoksa atla
            if predicted_id >= len(labels):
                continue

            if confidence > 0.3:
                # Bounding box
                box = object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
                (center_x, center_y, box_width, box_height) = box.astype("int")

                start_x = int(center_x - (box_width / 2))
                start_y = int(center_y - (box_height / 2))

                ids_list.append(predicted_id)
                confidences_list.append(float(confidence))
                boxes_list.append([start_x, start_y, int(box_width), int(box_height)])

    # Non-Maximum Suppression
    max_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)
    if max_ids is not None:
        if isinstance(max_ids, tuple):
            max_ids = list(max_ids)
        elif hasattr(max_ids, "flatten"):
            max_ids = max_ids.flatten().tolist()

        for max_id in max_ids:
            if isinstance(max_id, (list, tuple, np.ndarray)):
                max_class_id = int(max_id[0])
            else:
                max_class_id = int(max_id)

            box = boxes_list[max_class_id]
            start_x, start_y, box_width, box_height = box

            predicted_id = ids_list[max_class_id]
            label = labels[predicted_id]
            confidence = confidences_list[max_class_id]

            end_x = start_x + box_width
            end_y = start_y + box_height

            box_color = [int(c) for c in colors[predicted_id]]

            label_text = "{}: {:.2f}%".format(label, confidence*100)
            print("predicted object {}".format(label_text))

            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), box_color, 2)
            cv2.putText(frame, label_text, (start_x, start_y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 2)

    cv2.imshow("Mask Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
