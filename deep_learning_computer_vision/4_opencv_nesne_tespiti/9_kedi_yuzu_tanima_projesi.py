import cv2
import os

files = os.listdir(r"C:\Users\seyma\Desktop\media\kediler")
print(files)
img_path_list = []
for f in files:
    if f.endswith(".jpg"): 
        img_path_list.append(f)
print(img_path_list)

#klasördeki her resimde tek tek dolaşır 
for j in img_path_list:
    print(j)
    image = cv2.imread(os.path.join(r"C:\Users\seyma\Desktop\media\kediler", j))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #kedileri tespit eder
    detector = cv2.CascadeClassifier(r"C:\Users\seyma\Desktop\opencv_bolumu\cascade\haarcascade_frontalcatface.xml")
    rects = detector.detectMultiScale(gray, scaleFactor = 1.045, minNeighbors = 2)
    
    for (i, (x,y,w,h)) in enumerate(rects):
        cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,255),2)
        cv2.putText(image, "Kedi {}".format(i+1), (x,y-10),cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0,255,255),2)
        
    cv2.imshow(j, image)
    if cv2.waitKey(0) & 0xFF == ord("q"): continue

cv2.destroyAllWindows()