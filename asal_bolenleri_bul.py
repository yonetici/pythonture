import sys


def asalBolenleriBul(x):
    try:
        x = int(x)
    except ValueError:
        print("Invalid Input")
        sys.exit(1)
    if x<0:
        print("Negatif sayı olamaz.")
        sys.exit(1)
    asalBolenler = []
    for i in range(2,x):
        if(x % i == 0):
            asalBolenler.append(i)
            x = x / i
        else:
            i = i + 1
    return asalBolenler

#usage print(asalBolenleriBul(input("Sayi: ")))
