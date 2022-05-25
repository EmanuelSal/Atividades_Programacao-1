def diferenca_listas(lista1, lista2):
    for valor1 in range(len(lista1) -1, -1, -1):
        for valor2 in lista2:
            if lista1[valor1] == valor2:
                lista1.pop(valor1)
                break
    return lista1
   
        
lista1 = [2, 1, 3, 4]
lista2 = [2]
diferenca_listas(lista1, lista2) == [1, 3, 4]
assert lista1 == [1, 3, 4]

lista1 = [1, 3, 4]
lista2 = [4]
diferenca_listas(lista1, lista2) == [1, 3] 
assert lista1 == [1, 3]

