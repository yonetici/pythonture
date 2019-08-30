class ogrenci:
    ad = "Ömer Faruk"
    soyad = "Bilgin"

    def yazdir(self):
        print(self.ad)
        print(self.soyad)
    
    def ortalama(self,vize,final):
        return vize*0.4+final*0.6

nesne = ogrenci()

print(nesne.ad," - ",nesne.soyad)

nesne.yazdir()

print("Ortalama: ", nesne.ortalama(47,87))


#Constructor (Yapıcı) Fonksiyonlar

class dortgen:
    def __init__(self,genislik,yukseklik): #Constructor
        self.genislik = genislik
        self.yukseklik = yukseklik
    def alan(self):
        return self.genislik*self.yukseklik

dikdortgen = dortgen(15,40)
print(dikdortgen.alan())

#Encapsulation // Kapsülleme

class urun:
    def __init__(self):
        self.__fiyat = 1000 #Kapsullendi. setter ile değişebilir.
    def fiyatYaz(self):
        print("Urun Fiyatı: ", self.__fiyat)
    def setFiyat(self,fiyat):
        self.__fiyat = fiyat

helva = urun()
helva.fiyatYaz()

helva.__fiyat=900

helva.fiyatYaz() # Fiyat halen 1000 yazar. Kapsüllendiği için dışarıdan değer atanamaz.
helva.setFiyat(999)
helva.fiyatYaz()

#Inheritance // Miras alma

class kus:  #Super Sınıf
    tur_ad=""
    kus_ad=""

    def isimYaz(self):
        print("Tur adı: ", self.tur_ad)
        print("Kuş adı: ", self.kus_ad)
class yirtici(kus): #Alt sınıf / Sub Class
    kanat_uuznlugu = "0"
    agirlik = "0"

class kartal(yirtici):
    alt_tur = ""

anadolu_kartali = kartal()

anadolu_kartali.tur_ad = "Anatolian Eagle"
anadolu_kartali.kus_ad = "Karabaş"
anadolu_kartali.kanat_uuznlugu = 4
anadolu_kartali.agirlik = 3.5
anadolu_kartali.alt_tur = "Aegean Black Eagle"

anadolu_kartali.isimYaz()

#Polymorphism // Çok biçimlilik

class kedi:
    def ses(self):
        print("Miyav")
class kopek:
    def ses(self):
        print("Hav hav")
class kus:
    def ses(self):
        print("Cik cik")

def hayvanSesi(hayvan):
    hayvan.ses()

ke = kedi()
ko = kopek()
ku = kus()

hayvanSesi(ke)
hayvanSesi(ko)
hayvanSesi(ku)




