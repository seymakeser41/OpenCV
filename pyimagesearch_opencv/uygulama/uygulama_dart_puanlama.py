import cv2
import numpy as np
import os
import pandas as pd
import math

# Görsel dosya yolları
paths = [
    r"C:\Users\seyma\Desktop\media\uygulama1\1.png", r"C:\Users\seyma\Desktop\media\uygulama1\2.png", r"C:\Users\seyma\Desktop\media\uygulama1\3.png", 
    r"C:\Users\seyma\Desktop\media\uygulama1\4.png", r"C:\Users\seyma\Desktop\media\uygulama1\5.png"]


#manuel olrak hesaplandı ve tespit edildi
#radius=[49,109,165,219,275]
#x,cy=300,300
def is_point_between_two_circles(x, y, center_x, center_y, r1, r2):
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    inner = min(r1, r2)
    outer = max(r1, r2)
    return inner < distance <= outer
# Puan hesaplayan fonksiyon
def calculate_score(px, py, s):
    if is_point_between_two_circles(px, py, cx, cy, 0, radius[0]):
        print(f"{s} atis 1 puan .")
        return 1
    if is_point_between_two_circles(px, py, cx, cy, radius[0], radius[1]):
        print(f"{s} atis 2 puan .")
        return 2
    if is_point_between_two_circles(px, py, cx, cy, radius[1], radius[2]):
        print(f"{s} atis 3 puan .")
        return 3
    if is_point_between_two_circles(px, py, cx, cy, radius[2], radius[3]):
        print(f"{s} atis 4 puan .")
        return 4
    if is_point_between_two_circles(px, py, cx, cy, radius[3], radius[4]):
        print(f"{s} atis 5 puan .")
        return 5
    else:
        print(f"{s} atis 0 puan .")
        return 0

# Atış puanlarını ve sonuç görsellerini tut
shot_scores = []
output_images = []
s=0
for i in range(1, len(paths)):
    radius=[49,109,165,219,275]
    cx,cy=300,300
    ref_img = cv2.imread(paths[i-1], cv2.IMREAD_GRAYSCALE)
    new_img = cv2.imread(paths[i], cv2.IMREAD_GRAYSCALE)
    diff = cv2.absdiff(ref_img, new_img)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = cv2.cvtColor(new_img.copy(), cv2.COLOR_GRAY2BGR)
    max_score = 0
    #for cnt in contours:
    for cnt in contours:
        s+=1
        if cv2.contourArea(cnt) > 50:
            x, y, w, h = cv2.boundingRect(cnt)
            center_x,center_y = (x + w // 2, y + h // 2)
            score = calculate_score(center_x,center_y,s)
            max_score = max(max_score, score)
            color = (0, 0, 255)
            cv2.rectangle(result, (x, y), (x + w, y + h), color, 2)
            cv2.putText(result, f"{score} puan", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            cv2.imshow(f"resim {i}",result)
            cv2.waitKey(0)
            
        
    shot_scores.append((i, max_score))
    output_images.append(result)
    last_img = new_img.copy()
    