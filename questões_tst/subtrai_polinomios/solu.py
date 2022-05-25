
# PROG1 - UFCG 
# MATRICULA: 120210785 | DATA: 10/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA 
# PROGRAMA QUE SUBTRAI OS POLINOMIOS


def subtrai_polinomios(p1,p2):
    
    
    diferenca = len(p2) - len(p1)
    maior = p2
    saida = []
    tamanho = len(p1)
    if tamanho > len(p2):
        tamanho = len(p2)
        diferenca = len(p1) - len(p2)
        maior = p1
        
    for valor in range(len(p1)):
        subtracao = p1[valor] - p2[valor]
        if(subtracao != 0):
            saida.append(p1[valor] - p2[valor])
    
    for i in range(diferenca):
        saida.append((maior[len(p1) + i]) * -1)
    
    return saida


p1 = [-5, 4, 3]
p2 = [-1, 0, 2, 0, 0, 0, 5]
assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

p1 = [-5, 4, 3]  # 3x2 + 4x - 5
p2 = [-4, 2, 3]  # 3x2 + 2x - 4
assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1

