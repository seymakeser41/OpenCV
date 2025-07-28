import cv2
import matplotlib.pyplot as plt

# template matching: sablon esleme

img = cv2.imread(r"C:\Users\seyma\Desktop\media\kopek.jpg", 0)
print(img.shape)
template = cv2.imread(r"C:\Users\seyma\Desktop\media\kopek_face.jpg", 0)
print(template.shape)
h, w = template.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    
    method = eval(meth)
    
    # Şablon eşleştirme işlemi: kaynak img üzerinde template'in en iyi eşleştiği konumları hesaplar
    res = cv2.matchTemplate(img, template, method)
    
    # Elde edilen karşılık matrisinin (eşleşme sonuçları) boyutunu yazdırır
    print(res.shape)
    
    # Elde edilen eşleşme matrisinden minimum ve maksimum değerleri ve bunların konumlarını bulur
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Eğer kullanılan yöntem düşük değerlerin daha iyi eşleşme olduğunu belirtiyorsa (örn: kare fark)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc  # En düşük değerin konumu en iyi eşleşme
    else:
        top_left = max_loc  # En yüksek değerin konumu en iyi eşleşme
    
    # Eşleşme sonucunda bulunan bölgenin sağ alt köşesini hesapla (şablonun boyutuna göre)
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    # Kaynak görüntü üzerinde bulunan eşleşme bölgesine dikdörtgen çiz
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap = "gray")
    plt.title("Eşleşen Sonuç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap = "gray")
    plt.title("Tespit edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()