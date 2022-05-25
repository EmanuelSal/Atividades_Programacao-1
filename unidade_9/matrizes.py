m =[ [ 10, 20, 30, 40] , [50, 60, 70, 80], [1, 2, 3, 4]]

soma = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        soma += m[i][j]

print(soma)

print("________")

soma = 0
for j in range(len(m[0])):
    for i in range(len(m)):
        soma += m[i][j]

print(soma)

print("________")

#CONTANDO OS PARES

cont = 0
for j in range(len(m[0])):
    for i in range(len(m)):
        if m[i][j] % 2 == 0:
            cont += 1
#MULTIPLIQUE OS PARES POR 10
for j in range(len(m[0])):
    for i in range(len(m)):
        if m[i][j] % 2 == 0:
            m[i][j] *= 10

print(m)
print(cont)

print("________")

#PARA MATRIZES QUADRADAS
soma = 0
for i in range(len(m)):
    soma += m[i][i] #SOMANDO A DIAGONAL
    m[i][i] = -10 #TROCANDO A DIAGONAL POR -10 (TODOS OS ELEMENTOS DA DIAGONAL)

print(m)
print(i, i)
print(soma)

print("_________")
# POR LINHA:
for i in range()
