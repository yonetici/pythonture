x = 2 # global

def fonksiyon():
    x = 5 # local değişken, sadece fonksiyon içinde kullanılır.
    print("İç değer: ", x)

fonksiyon()

print("Dışarı değer: ", x)

sayi = 10 #Global Değişken

def f2():
    global sayi
    sayi = sayi*2
    print("Sayi değeri: ", sayi)

f2()