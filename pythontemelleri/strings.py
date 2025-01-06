#STRİNG 
name="seyma" #string şeklinde değişken tanımladım 
surname="keser"#tırnkalar önemli tek veya çift olabilir
age=18

print("my name is"+ name+"" + surname + "and \n i am "+ str(age) + " years old.")
#age değişkenini yazdırıken tür dönüşümü yapmak gerekir
#\n bizi alt satıra geçirir 
selam="my name is"+ name+"" + surname + "and \n i am "+ str(age) + " years old."
print(selam) #tüm her şey bir değişkende toplanarak da aynı sonucu verir
print(selam[3]) #string değerler bir dizizdir ve elemanlarına indekslerle ulaşılabilir. başatn 0 ile başlar artarak gider
print(len(selam)) #dizinin uzunluğunu bize verir 
print(selam[-1]) #dizi sondan indeksleirse -1 ile başlar azalarak gider
print(selam[2:5]) #dizinin 2. indeksinden 5.indekse kadar yazar 5 dahil değil. 
#başlangıç ve bitiş belirtilmezse baştan veya sona kadar yazar (hangisi belirtilmediyse)
print(selam[2:20:2]) #2. indeksten 20. indekse kadar ikişer ikişer gider (1 atlar)

#STRİNG FORMATLAMA
print("my name is {1} {0}and i'm {2}".format(name,surname,age))#formatla süslü parantez içine gelecek olan şey yazdırılabilir
# format içindeki sırada indeks gibi süslü parantez içinde çağırılabilir
# age değişkeninde tür dönümüne gerek kalmaz çünkü toplama yok
result=200/700
print("the result is {r:5.4}".format(r=result))
#virgülden sonra 4 basamak olacak şekilde,sayı için 5(tam kısım) yer ayıracak şekilde tür dönüşümü yapmadan sonucu yazdırdık
print(f"my name is {name} {surname} and i'm {age}")#format kolaylığını sadece f diyerek de kullanabiliriz

