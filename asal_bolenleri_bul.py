def asal_bolenleri_bul(no):
    i = 2
    asallar = []
    cikti = set()
    while i <= no:
        if (no % i) == 0:
            asallar.append(i)
            no = no / i
        else:
            i = i + 1
    for x in asallar:
        cikti.add(x)
    return cikti

#usage print (asal_bolenleri_bul(987654))