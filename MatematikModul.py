def topla (sayi1,sayi2):
    print("Toplam: " + str(sayi1 + sayi2))
def carp (sayi1,sayi2):
    print("Çarpım: " + str(sayi1 * sayi2))

customer = {
    "firstName" : "Yusuf Emin",
    "lastName" : "Bilgin"
}

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

