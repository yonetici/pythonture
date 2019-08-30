
number = int(input("sayi girin: "))
check = True
for x in range(2, number):
    if (number % x == 0):
        check = False
        break
if check == False:
    print("Asal değil")
else:
    print("Sayımız Asal")