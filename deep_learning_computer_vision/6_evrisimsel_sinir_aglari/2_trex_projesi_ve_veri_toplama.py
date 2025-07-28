#veri toplama 

import keyboard #klavye tuşlarını kullanarak veri toplamaya yarar
import uuid  #görüntü kayıt almak için gerekli
import time 
from PIL import Image
from mss import mss

# http://www.trex-game.skipser.com/  -> veri toplanacak site

mon={"top":550, "left":700, "width":250, "height":100}  #ekranda görüntü alacağımız bölgeyi belirleyen koordinatlar
sct=mss() #veileri toplayacak

i=0

def record_screen( record_id, key):
    global i #kaç kez klavyeye bastığımızı belirtir

    i+=1
    print("{}: {}".format(key,i)) #key=klavyeden basılan anahtar
    img=sct.grab(mon) #görüntü olarak alır 
    im= Image.frombytes("RGB",img.size, img.rgb) #resmi oluşturur

    save_path = "C:/Users/seyma/Desktop/media/trex_veri"
    im.save("{}/{}_{}_{}.png".format(save_path, key, record_id, i))  #resmi kaydeder

is_exit=False

#veri toplamayı bırakmak için kullanılacak fonksiyon
def exit ():
    global is_exit
    is_exit=True

keyboard.add_hotkey("esc", exit)

record_id=uuid.uuid4()

while True:
    if is_exit: break

    try:
        if keyboard.is_pressed(keyboard.KEY_UP): #eğer klavyeden yukarı tuşuna basıldıysa uygulanacaklar
            record_screen(record_id, "up")  #kaydetti
            time.sleep(0.1) #hızı dengeler
        elif keyboard.is_pressed(keyboard.KEY_DOWN): #eğer klavyeden aşağı tuşuna basıldıysa uygulanacaklar
            record_screen(record_id, "down")  #kaydetti
            time.sleep(0.1) #hızı dengeler
        if keyboard.is_pressed("right"): #eğer klavyeden ileri tuşuna basıldıysa uygulanacaklar, hiçbir şey yapmama durumu 
            record_screen(record_id, "right")  #kaydetti
            time.sleep(0.1) #hızı dengeler

    except RuntimeError:continue  #try bloğundaki kodların hata vermesi durumunda hatayı belirtip devam etmesini sağlar

