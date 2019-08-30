#Created By 'Samarth Dangat'.


from math import sqrt 

a= int(input("İlk kenarın ölçüsü: "))
b = int(input("İkinic kenarın ölçüsü: "))

print("Pisagor Teoremi")
print("Bu teorem ile iki kenarı bilinen üçgenin hipotenüs ölçüsünü bulabilirsiniz.\n\n")
print("ABC üçgeninde AC hipotenüsü temsil etmektedir.\n")
print("AB =", a)
print("BC =", b)
num = a**2 + b**2
sum = sqrt(num)
print("____________________________\n")
print("Sonuç: AC =" , sum , "\n")
print("____________________________\n")