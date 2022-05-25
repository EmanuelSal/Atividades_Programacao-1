# coding: UTF-8
# PROGRAMAÇÃO 1 - UFCG - MINITESTE 8
# MATRÍCULA: 120210785 | DATA: 24/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE ENCONTRE AS OCORRENCIAS UNICAS EM COMUM EM DUAS SEQUENCIAS


def unicos_em_comum(seq1, seq2):
    letras = ["A", "B", "C", "D"] # LISTA COM AS LETRAS

    
    count1 = [0, 0, 0, 0] # CONTADOR DA SEQUENCIA 1:
    for letra in seq2:
        
        if letra == "A":
            count1[0] += 1
        if letra == "B":
            count1[1] += 1
        if letra == "C":
            count1[2] += 1
        if letra == "D":
            count1[3] += 1
    
    letras = ["A", "B", "C", "D"]
    count2 = [0, 0, 0, 0] # CONTADOR PARA A SEQUENCIA 2:
    for letra in seq1:
        
        if letra == "A":
            count2[0] += 1
        if letra == "B":
            count2[1] += 1
        if letra == "C":
            count2[2] += 1
        if letra == "D":
            count2[3] += 1
    
    iguais = []
    for i in range(len(count1)):
       # CHECANDO SE TEM APENAS UMA OCORRENCIA:
        if count2[i] == 1 and count1[i] == 1:
            iguais.append(letras[i])
        elif count1[i] == 1 and count2[i] == 1:
            iguais.append(letras[i])

    
    # RETORNA A LISTA APENAS COM OS IGUAIS EM COMUM DAS DUAS SEQUENCIAS:
    return iguais




seq1 = [ 'A', 'A', 'B', 'C', 'C', 'D']
seq2 = ['B', 'A', 'C', 'D', 'D']
assert unicos_em_comum(seq1, seq2) == ['B']
seq1 = ['A', 'A', 'B', 'C']
seq2 = ['A', 'B', 'C']
assert unicos_em_comum(seq1, seq2) == ['B', 'C']