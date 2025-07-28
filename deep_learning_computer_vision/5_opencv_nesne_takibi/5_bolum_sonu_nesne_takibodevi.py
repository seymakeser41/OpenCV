#önceki kodları kullanarak farklı nesne takip algoritmalarını kullanın ve algoritmaların karşulaştırmasını yazın 

"""
1. BOOSTING
Adaboost tabanlıdır (Haar-like özellikler).

Görüntüdeki küçük değişimlerde bile başarısız olabilir.

Kullanımı önerilmez; modern alternatifleri mevcut.

2. MIL (Multiple Instance Learning)
Nesne konumunu tahmin etmek için pozitif ve negatif örnekleri kullanır.

Nesne kısmen görünse bile çalışabilir.

Ancak yüksek hızda hareket eden nesnelerde stabil değildir.

3. KCF (Kernelized Correlation Filters)
MOSSE'ye göre daha doğrulukludur.

Çok hızlı çalışır ancak nesnenin ölçek değiştirdiği durumlarda sorun yaşar.

Tek nesne takibi için idealdir.

4. TLD (Tracking-Learning-Detection)
Takip + öğrenme + tespit bileşenlerinden oluşur.

Öğrenme sistemi zamanla hatalı örnekleri öğrenirse performans düşer.

Günümüzde çok tercih edilmez.

5. MedianFlow
Gerçekten kararlı bir takip algoritmasıdır.

Ancak nesne sahneden çıkarsa veya görünümü çok değişirse "crash" olabilir.

Hataları anlamak için analiz araçlarında kullanılır.

6. MOSSE
Çok düşük donanımlarda bile gerçek zamanlı çalışabilir.

Görüntü kalitesi bozulursa veya arka plan çok değişirse hatalı takip yapar.

Basit uygulamalarda kullanılır.

7. CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability)
En doğru çalışan klasik OpenCV algoritmasıdır.

ROI (nesne) konumunu net tespit eder, boyut ve şekil değişimlerine uyumludur.

Gerçek zamanlı çalışması için güçlü CPU gerekir.
"""

#İhtiyacın	                             En Uygun Algoritma
#Gerçek zamanlılık (çok hızlı çalışsın)	   MOSSE veya KCF
#Yüksek doğruluk	                            CSRT
#Sabit kamera, az hareket	                  MedianFlow
#Öğrenme + takip (gelişmiş)                  	TLD
#Kısıtlı donanım (örneğin Raspberry Pi)	        MOSSE
import cv2

#yorum satırı olanlar artık eski olduğu için desteklenmiyor
OPENCV_OBJECT_TRACKERS = {
    "boosting": cv2.legacy.TrackerBoosting_create,
    "mil": cv2.legacy.TrackerMIL_create,
    "kcf": cv2.legacy.TrackerKCF_create,
    "tld": cv2.legacy.TrackerTLD_create,
    "medianflow": cv2.legacy.TrackerMedianFlow_create,
    "mosse": cv2.legacy.TrackerMOSSE_create,
    "csrt": cv2.legacy.TrackerCSRT_create
}
    
tracker_name = "boosting"

trackers = cv2.legacy.MultiTracker_create()


video_path = r"C:\Users\seyma\Desktop\media\MOT17-04-DPM.mp4"
cap = cv2.VideoCapture(video_path)

fps = 30     
f = 0
while True:
    
    ret, frame = cap.read()
    if not ret or frame is None:
       print("❌ Video okunamadı veya bitti.")
       break
    (H, W) = frame.shape[:2]
    frame = cv2.resize(frame, dsize = (960, 540))
    
    (success , boxes) = trackers.update(frame)
    
    info = [("Tracker", tracker_name),
        	("Success", "Yes" if success else "No")]
    
    string_text = ""
    
    for (i, (k, v)) in enumerate(info):
        text = "{}: {}".format(k, v)
        string_text = string_text + text + " "
    
    cv2.putText(frame, string_text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
    for box in boxes:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("t"):
        
        box = cv2.selectROI("Frame", frame, fromCenter=False)
    
        tracker = OPENCV_OBJECT_TRACKERS[tracker_name]()
        #birden fazla tracer olduğu için birden fazla nesneyi takip edebiliyoruz
        trackers.add(tracker, frame, box)
    elif key == ord("q"):break

    f = f + 1
    
cap.release()
cv2.destroyAllWindows() 