def selamlasma(kisi, soyisim = "Dostum"):
    print("Merhaba " + kisi + " " + soyisim)

selamlasma("Kamil")
selamlasma("Salih", "Bilgin")

def dikUcgenAlani(a, b):
    return int((a*b)/2)
alan = dikUcgenAlani(6,8)
print(alan)

#Lamba Fonksiyon
# fonksiyon_ismi = lambda degisken : islem

dikUcgenAlan = lambda a, b : (a*b)/2
print("Lamba örnek 1:")
print(int(dikUcgenAlan(7,4)))

ikiKat = lambda x: x*2

print("Lamba örnek 2:")
print(ikiKat(454))

liste = [1,2,5,6,11,191,34,62,75]

yeni_liste = list(filter(lambda x : (x%2==1 or x%17==0), liste))

print("Lamba örnek 3:")
print(yeni_liste)

yeni_liste2 = list(map(lambda x: (x**2), yeni_liste))

print("Lamba örnek 4:")
print(yeni_liste2)

print("Lamba Örnek 5:")
mx = lambda x,y : x if x>y else y
print(mx(6,7))
