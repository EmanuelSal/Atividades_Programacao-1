def inverte3a3(string):
    lista = []
    contador = 0
    concatena = ""
    saida = ""

    for s in range(len(string)):
        concatena += string[s]
        contador += 1

        if contador % 3 == 0:
            lista.append(concatena)
            concatena = ""

    for palavra in range(len(lista) -1, -1, -1):
        saida += lista[palavra]

    return saida


assert inverte3a3("limaelima") == "imaaellim"
assert inverte3a3("abcdef") == "defabc"

