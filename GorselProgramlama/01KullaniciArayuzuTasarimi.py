#GUI - Kullanıcı Arayüzü Tasarımı

import tkinter as tk #Tk kütüphanesi çağrılır.
pencere = tk.Tk()

#Tasarım ve kodlar bu bölümde yazılıyor.

pencere.title("İlk arayüz programı")
#Açılan pencereyi ekranda yatay ve dikeyde ortalamak için
#Google'dan aldığım kodlar.
#https://yagisanatode.com/2018/02/24/how-to-center-the-main-window-on-the-screen-in-tkinter-with-python-3/

windowWidth = pencere.winfo_reqwidth()
windowHeight = pencere.winfo_reqheight()
positionRight = int(pencere.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(pencere.winfo_screenheight()/2 - windowHeight/2)

#Pencereye label ekleme
etiket = tk.Label(text="Etiket - Label", font = "Verdana 22 bold")
#İlk Yöntem pack(): komponentleri ikişerli üçerli butonu , labeli
#bir arada kullanmanızı sağlar. Komponenleri paketler.
etiket.pack()
#İkinci Yöntem grid(): Arayüzün parçalara bölündüğünü kabul eder.
#Örneğin 3 satır 5 sütun. Labelleri yerleştirir.
#Üçüncü Yöntem place(): x,y koordinatları ile sizin yerleştirmenizi sağlar.
#pencere.geometry("500x300+400+400") #Veri string alınıyor. (EnxBoy+Xkoordinat+YKoordinat)
pencere.geometry("500x300+{}+{}".format(positionRight, positionDown))
pencere.mainloop()
