# PROGRAMACAO 1 - UFCG - REPOSICAO
# MATRICULA: 120210785 | DATA: 30/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA: FUNCAO QUE SOME OS VALORES DAS POSICOES SIMETRICAS

def soma_simetricos(valores):
    # Ele pede que retorne uma lista nova
    lista = []
    tamanho = len(valores) # Variavel para o tamanho da lista de entrada
    
    # Se a lista inicial for tamanho par:
    if tamanho % 2 == 0:
        for valor in range(len(valores)//2):
            somatorio = 0
            # Somatorio para dos valores
            somatorio += valores[valor] + valores[len(valores) -1 -valor]
            lista.append(somatorio) # Append na nova lista
    
    # Se a lista inicial for de tamanho impar:
    elif tamanho % 2 != 0:
        for valor in range(len(valores)//2) :
            somatorio = 0
            # Somatorio para os valores:
            somatorio += valores[valor] + valores[len(valores) -1 -valor]
            lista.append(somatorio) # Append na nova lista
        
        lista.append(valores[(tamanho//2)])

    return lista # Retornando a nova lista 

assert soma_simetricos([2, 5, 3, 9]) == [11, 8]
assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]
assert soma_simetricos([3, 8, 5, 10, 9]) == [12, 18, 5]
assert soma_simetricos([8, 2, 2, 8]) == [16, 4]
assert soma_simetricos([8, 2]) == [10]
assert soma_simetricos([8]) == [8]
