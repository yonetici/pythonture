x = [[3, 5, 6], [4, 22, 3], [8, 2, 8]]
y = [[2, 9, 2], [2, 1, 12], [9, 43, 2]]

sonuc = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]



for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j] + y[i][j]

print(sonuc)
