"""
CNN mimarisi:
evrisim katmani + piksel ekleme katmani + tam baglanti (sayilar degisir)
(öz nitelik cikarma kismi)                 (siniflandirma)
evrisim katmani: filtre kullanilarak özellik haritasi olusturur, sonunda aktivasyon fonksiyonu uygulanir
piksel eklmeme katmani : filtre sonucu azalan boyutu dengeler
yüksek seviye katmanlarda resmin ayirt edici özellikleri daha cok tespit edilir
aktivasyon fonk: modelin dogrusal olmayan yapilarini ögrenmesini sagliyor
ortaklama: degismeyen özelliklerin algilanmasini saglar ve ezberleyi kontrol eder 
düzlestirme: iki boyutlu veriyi vektör haline getirme 
seyreltme(dropout): rastgele secilen nöronlarin eğitimde göz ardi edilmesidir , ezberlemeyi önler 
veri artirma: ezberlemeyi önlemek icin veri artirilir, ölcekler, döndürmeler , ortalamalar yapilir


"""