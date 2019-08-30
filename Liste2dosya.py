aile = ["Salih","Rıdvan","Şaban","Güner"]
fileToAppend = open("aile.txt","w")

for birey in aile:
    fileToAppend.write(birey)
    fileToAppend.write("\n")

fileToAppend.close()