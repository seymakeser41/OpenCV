#8_
#özgül model geliştirme 
#cpu: maliyet düşük zaman kaybı
#gpu: maliyet yüksek zaman kaybı yok 

#google colab kullanmak en mantıklısı 

#Darknet framework indir githuptan 
#-veri topla 
#-verileri düzenle (format)
#-veri etkiletme (make sense )
#- eğitim 

#9_DARKNET KURALIM 

"""
git scm / download indir kur 
github.com/AlexeyAB/darknet  açılan dosyada sağ tık fit push here git clone ... (yolu kopyala)  
makfile GPU=1, CUDNN=1, OPENCV=1 yap kaydet kapat 

eğitim ve test için transfer learning yapar ve bunun için githubtan conv ara yolov4.conv.137  indir 

aynı siteden control+ f yolov4.weigh  yolov4.weigh indir 

cfg klasörüne git yolov4.cfg dosyasını kopyala açtığın klasöre kopyala ulaşım kolaylığı için 
bu dosyayı aç subdivisions=64 , width, height =416 , max_batches=2000, steps=1800  tıkla kontrol+f ile class ara classes=1 , filters=18(classın 5 fazlasının 3 katı) tüm class ve filtrelere uygula kaydet ve kapat 


"""

