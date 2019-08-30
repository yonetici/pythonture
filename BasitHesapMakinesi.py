from MatematikModul import basithesapmakinesi
"""
class basithesapmakinesi:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
    def topla(self):
        return self.sayi1 + self.sayi2
    def cikar(self):
        return self.sayi1 - self.sayi2
    def carp(self):
        return self.sayi1 * self.sayi2
    def bol(self):
        return self.sayi1 / self.sayi2


"""
print("İşlem?")
print("1 -> Topla")
print("2 -> Çıkar")
print("3 -> Çarp")
print("4 -> Böl")

islem = int(input("İşlem numarası girin:"))

sayi1 = int(input("İlk sayısı girin: "))
sayi2 = int(input("İkinci sayısı girin: "))

hesapla = basithesapmakinesi(sayi1,sayi2)

if islem == 1:
    print(hesapla.topla())
elif islem == 2:
    print(hesapla.cikar())
elif islem == 3:
    print(hesapla.carp())
elif islem == 4:
    print(hesapla.bol())
else:
    print("Hatalı seçenek")
