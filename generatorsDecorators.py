

def uretece():
    sayi = 0
    print(sayi, ". adım")
    yield sayi # yield return yerine kullanılır.
    sayi +=1
    print(sayi, ". adım")
    yield sayi
    sayi +=1
    print(sayi, ". adım")
    yield sayi
    sayi +=1
    print(sayi, ". adım")
    yield sayi
a = uretece()
next(a)
next(a)
next(a)
next(a)
#next(a) stopiteration hatası alındı.

b = uretece()

for x in b:
    next(b)

#Decorator'lar argüman olarak fonksiyon alıp,
#sonuçta yine fonksiyon döndüren fonksiyonlardır.

def linkYap(f):
    def yaz():
        return "<a href='https://www." + f() + ".com</a>Link</a>"
    return yaz

def adres():
    return "google"

a = linkYap(adres)
print(a())
#İkinci tür kullanımı
@linkYap #Fonksiyonu decorator'a bağlıyoruz.
def adr():
    return "turkwm"
print(adr())

