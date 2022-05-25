# DUPLICA LISTA
def duplica(lista):
    for i in range(len(lista)):
        lista[i] = 2 * lista[i]

l = [1, 2, 3, 4, 5]
l1 = [1, 2, 2, 3, 4, 5]

# CONTADOR
def conta(lista):
	
	x = 2
	count = 0
	for i in range(len(lista)):
		if lista[i] == x:
			count += 1
	return count

# REMOVE ELEMENTO - POP
def meu_remove(lista, e):
    for i in range(len(lista)):
        if lista[i] == e:
            lista.pop(i)
            return lista
            
# REMOVE 2 = POP
def meu_remove_2(lista, e):
    for i in range(len(lista) -1, -1, -1):
        if lista[i] == e:
            lista.pop(i)
    return lista

# FUNÇÃO EXTEND
def meu_extend(lista1, lista2):
    for elemento in lista2:
        lista1.append(elemento)
    return lista1

# CONCATENAR LISTAS
def concatena(lista1, lista2):
    lista1 += lista2

concatena(l, l1)
print(l)
print(l1)