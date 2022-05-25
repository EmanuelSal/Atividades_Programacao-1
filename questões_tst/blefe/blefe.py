# PROG1 - UFCG
# MATRICULA: 120210785 | DATA: 17/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA

def blefe(lista1):
    lista = []
    
    for valor in range(len(lista1)):
        if valor != 0:
            if lista1[valor] > lista1[valor -1]:
                lista.append(lista1[valor] - lista1[valor - 1])
                lista1[valor] = lista1[valor - 1]
            
            else:
                lista.append(0)
        else:
            lista.append(0)
    
    return lista