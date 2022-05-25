def slice(lista):
    nova_lista = []
    for i in range(2, len(lista)):
        nova_lista.append(lista[i])
    return nova_lista


def ordena(lista):
    nova_lista = []
    tamanho = len(lista)
    while len(nova_lista) < tamanho:
        maior = lista[0]
        index = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                index = i

        lista.pop(index)
        nova_lista.append(maior)
    return nova_lista

def noves_fora(lista):

    evolucao = [lista]
    resultado = 0
    if len(lista) == 1:
        if lista[0] < 9:
            resultado = lista[0]
            return resultado, evolucao

        else:
            evolucao.append([0])
            return resultado, evolucao

    while True:
        if len(lista) == 1:
            if lista[0] < 9: break
            else:
                evolucao[1] = 0
                resultado = 0
                break

        resultado = (lista[0] + lista[1]) % 9
        lista = [resultado] + slice(lista)
        lista = ordena(lista)
        evolucao.append(lista)

    return resultado, evolucao



assert noves_fora([9, 7, 5, 4, 3, 1]) == (2, [[9, 7, 5, 4, 3, 1],
                                              [7, 5, 4, 3, 1],
                                              [4, 3, 3, 1],
                                              [7, 3, 1],
                                              [1, 1],
                                              [2]])

assert noves_fora([4]) == (4, [[4]])
assert noves_fora([9]) == (0, [[9], [0]])
assert noves_fora([9, 9]) == (0, [[9, 9], [0]])
