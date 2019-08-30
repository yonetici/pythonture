
# try:
#     sayi = int(input("sayi girin: "))
# except ValueError:
#     print("Lütfen sayı girin")
# except: ZeroDivisionError:
#     print("Payda sıfır olamaz")
# except:
#     print("Bir hata oluştu")

liste = ["davaro",12,0,"6"]

# işlem: tüm dataların çaprmaya göre tersi
import sys
for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuc: " + str(sonuc))
    except ValueError:
        print(str(x) + " bir sayı değil")
    except ZeroDivisionError:
        print(str(x) + " ile bölüm tanımsızdır.")
    except:
        print(str(x) + " icin sonuc hesaplanamadı.")
        print("Hata mesajı: " + str(sys.exc_info()[0]) + " " + str(sys.exc_info()[1]))
    finally: # try ya da except'in hangisi çalışırsa çalışsın, son olarak finally'in değeri döner.
        # Örneğin dosyalarla çalışırken hata oluştu. Dosya açık kaldı. Kapatma kodlarını finally'e yazabiliriz.
        print("Bitiş")
