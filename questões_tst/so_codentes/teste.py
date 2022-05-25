tam_c = int(input())
tam_linha = int(input())

matriz = []
linha = []

for j in range(tam_c):
    linha.append(0)
for i in range(tam_linha):
    matriz.append(linha)

print(matriz)

