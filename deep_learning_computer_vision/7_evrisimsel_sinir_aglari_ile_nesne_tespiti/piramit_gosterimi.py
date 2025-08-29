"""
piramit gösterimi: bir görüntünün farklı ölçeklerdeki görüntülerdeki nesneleri bulmamamizi sağlar
en başta orjinal resimken gittikçe belli ölçüde küçülür ve genelde gauss bulanıklaştirmayla düzleştirilir

"""

import cv2
import matplotlib.pyplot as plt

def image_pyramid(image, scale = 1.5, minSize=(224,224)):
    
    yield image #çok fazla resimden kaynaklana sorunu resimleri generate etti
    
    while True:
        
        w = int(image.shape[1]/scale) 
        image = cv2.resize(image, dsize=(w,w))#belirlenen oranda küçüldü
        
        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]: #küçültme sınırı kontrolü
            break
        
        yield image

#resim üzerinde deneme  
#      
# img = cv2.imread("husky.jpg")
# im = image_pyramid(img,1.5, (10,10))
# for i, image in enumerate(im):
#     print(i)
#     if i == 5:
#         plt.imshow(image)