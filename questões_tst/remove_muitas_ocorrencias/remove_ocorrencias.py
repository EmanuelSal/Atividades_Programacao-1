# PROG1 - UFCG
# MATRICULA: 120210785 | DATA: 10/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE REMOVE OCORENCIAS

def remove_muitas_ocorrencias(lista):

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1):
            if int(lista[j]) == int(lista[j + 1]):
               lista.pop(j)

def remove(lista):
    count = 0
    for i in range(len(lista) -1, -1, -1):
        x = lista[i]
        for valor in lista:
            if valor == x:
                count += 1
            if count > 2:
                lista.pop(i)


digitos = [1, 1, 2, 2, 5, 1]
remove(digitos)
print(digitos)