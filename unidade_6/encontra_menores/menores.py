def ordena(lista):
    for i in range(0, len(lista) -1):
        for j in range(len(lista) -1 -i):
            if int(lista[j]) > int(lista[j + 1]):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return(lista)

def encontra_menores(num, lista):
    ordena(lista)
    for valor in lista:
        if int(valor) < num:
            return valor

        elif int(valor) == num:
            return -1


lista1 = [100,200,300,400]
lista2 = [15, 12, 4, 9, 10]
lista3 = [10, 6, 4, 3]
assert encontra_menores(100, lista1) == -1
assert encontra_menores(10, lista2) == 4
assert encontra_menores(4, lista2) == -1
assert encontra_menores(4, lista3) == 3

