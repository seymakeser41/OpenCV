"""
you only look once
nesneleri ve koordinatlari ayni anda tespit eder(merkez, genişlik ve yükseklik)

önce bölgeye ayirir,  bounding box çizer, güven skoru hesaplar, non-maximum supperession ile gereksiz kutulari eler


CNN:nesne tespiti için kullanilir
1-resmi alir matrise çevirir
2-convolution katmaninda filtrelerle yaptiği hesaplamar sonucu resmi küçültür 
3-max pooling ile en büyük değere sahip alani alir
4-RELU ile negatif değerler elenir 
5-fully connected layer ile siniflandirma yapilir



"""