import numpy as np

sayilar2 = np.array([0,5,10,15,20,25,30])
sayilar = np.array([[0,5,10,15],[20,25,30]])

print(sayilar[0])
print(sayilar[1:2]) #Birinci satırın ikinci değeri
print(sayilar[:,0]) # Tüm satırların ikinci indexi
print(sayilar2[0:3])
print(sayilar2[2:])
print(sayilar[::-1])