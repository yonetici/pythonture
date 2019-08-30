
f = open("musteriler.txt","r") # default hali r. x,w,a kullanılabilir.
#r Read, a Append, w Write, x Create
#print(f.read())
print("***********")
print(f.readline()) #SAtır Satır okuma
print("***********")
for l in f:
    print(l)

f.close()

#Dosyaya yazma
fileToAppend = open("musteriler.txt","w")
fileToAppend.write = ("Salih")
fileToAppend.close()


#Dosya Silme
import os
os.remove("musteriler.txt")

#Dosya var mı Yok mu?
if os.path.exists("musteriler.txt"):
    os.remove("musteriler.txt") #Var sil dedim.
else:
    print("Dosya yok")

#Klasör Oluşturma / Silme

"""
os.mkdir("silinecekDizin")
os.rmdir("silinecekDizin")
"""