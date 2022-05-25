m =[ [ 10, 20, 30, 40] , [50, 60, 70, 80], [1, 2, 3, 4]]

nl = len(m)
nc = len(m[0])

# POR LINHAS:
for i in range(nl):
    for j in range(nc):
        print(i, j)

# POR COLUNAS:
for c in range(nc):
    for l in range(nl):
        print(c, l)

# MATRIZES QUADRADAS:
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
e1 = m2[0][0]
e2 = m2[1][1]
e3 = m2[2][2]

print("-" * 30)

# for i in range(len(m2)): #3
  #  print(m2[i][i])

for i in range(len(m2) -1): #3
    print(m2[i][i-i])
