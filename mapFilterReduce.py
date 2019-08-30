sayilar = [1,2,3,4,5]

sayilarKareli = []

for sayi in sayilar:
    sayilarKareli.append(sayi**2)

print(sayilarKareli)
print("***********")
#map ile

sayilarinKaresi = list(map(lambda x:x**2, sayilar))
print(sayilarinKaresi)
print("***********")
#Filter ile çalışma
sayilarFiltreli = list(filter(lambda x:x%2==0,sayilar))
#İkiye kalansız bölünen sayıları filtrele
print(sayilarFiltreli)

print("***********")
#Reduce ile çalışma
from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y: x*y,sayilar)
print(sayilarFaktoriyel)

print("***********")
#map dizi elemanlarının tamamına yapılacak işlemleri hızlandırır.
vizeNotlari = [20,45,68,70,83]
#Vize notlarına %20'de biz ekleyelim.
vizeNot = list(map(lambda x:x+x*20/100,vizeNotlari))
print(vizeNot)

finalNot = [90,20,41,15,70]

#Geçer notun 60 olduğu sistemde geçti mi kaldı mı ?
print(list(map(lambda x,y: (x*40/100+y*60/100), vizeNot,finalNot)))
print(list(map(lambda x,y: "Geçti" if (x*40/100+y*60/100)>60 else "Kaldı", vizeNot,finalNot)))




#lambda x: True if x % 2 == 0 else False


print("***********")
#Mapte fonksiyon kullanımı
def ikiKati(x):
    return x*2
def yari(x):
    return x/2
fonk = [ikiKati, yari]
for a in range(5):
    deger = list(map(lambda x:x(a), fonk))
    print(deger)
print("***********")
#Filter dizi elemanlarının seçilmesinde kullanılır.

vizeSec=list(filter(lambda x:x%5==0,finalNot))
print(vizeSec)
print("***********")
#Reduce tamamını etkileyen işlemler yapar. Toplanması, Çarpılması ..vs

toplam=reduce(lambda x,y: x+y, finalNot)
print(toplam)
print("***********")