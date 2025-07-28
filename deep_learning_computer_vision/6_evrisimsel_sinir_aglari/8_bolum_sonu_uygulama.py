import cv2
import pickle
import numpy as np
import os

# Sınıf isimlerini al
path = r"C:\Users\seyma\Downloads\archive\fruits-360_100x100\fruits-360\Training"
classNames = os.listdir(path)

# preprocess fonksiyonu
def preProcess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.equalizeHist(img)
    img = img / 255.0
    return img

# kamera ayarları
cap = cv2.VideoCapture(0)
cap.set(3, 480)
cap.set(4, 480)

# model yükle
with open("fruit360_model.p", "rb") as f:
    model = pickle.load(f)

while True:
    success, frame = cap.read()
    if not success:
        continue

    img = cv2.resize(frame, (32, 32))
    img = preProcess(img)
    img = img.reshape(1, 32, 32, 1)

    predictions = model.predict(img)
    classIndex = int(np.argmax(predictions))
    probVal = np.amax(predictions)

    if probVal > 0.7:
        cv2.putText(frame, f"Class: {classNames[classIndex]}, Prob: {probVal:.2f}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Fruit360 Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
