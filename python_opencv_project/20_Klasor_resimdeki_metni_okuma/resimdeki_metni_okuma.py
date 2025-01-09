#tesseract uygulaması kullanılacaktır
# https://github.com/UB-Mannheim/tesseract/wiki  adresinden indirin ve kurun ardından yolu sistem değişkenlerinden path e ekleyin

from PIL import Image
import pytesseract#kütüphaneleri ekledik
#bu şekilde resmi dahil ettik
img=Image.open("python_opencv_project/media/text.png")
#bu fonksiyon ile resimdeki ingilizce harfleri okuduk
text=pytesseract.image_to_string(img,lang="eng")
print(text)
