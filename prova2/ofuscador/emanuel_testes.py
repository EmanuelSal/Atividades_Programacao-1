def ofuscador(linha):
    for letra in range(len(linha)):
        if linha[letra] == "a" or linha[letra] == "A":
            linha[letra] = 4
        elif linha[letra] == "B" or linha[letra] == "b":
            linha[letra] = 8
        elif linha[letra] == "E" or linha[letra] == "e":
            linha[letra] = 3
        elif linha[letra] == "G" or linha[letra] == "g":
            linha[letra] = 6
        elif linha[letra] == "letra" or linha[letra] == "I":
            linha[letra] = 1
        elif linha[letra] == "L" or linha[letra] == "letra":
            linha[letra] = 7
        elif linha[letra] == "s" or linha[letra] == "S":
            linha[letra] = 5
        elif linha[letra] == "O" or linha[letra] == "o":
            linha[letra] = 0
        if linha[letra] == " ":
            linha[letra] = '*'

linha = "I love Python!"
print(ofuscador(linha))