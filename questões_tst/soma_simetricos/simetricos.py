# PROG1 - UFCG
# MATRICULA: 120210785 | DATA: 10/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE SOMA OS VALORES NAS POSIÇOES SIMETRICAS

def soma_simetricos(valores):
        
    lista = []
    calculo = 0
    if len(valores) % 2 != 0:
        tamanho = int(len(valores)//2)
        for t in range(tamanho + 1):
            if t == 0:
                calculo = int(valores[t]) + int(valores[len(valores)- 1]) 
                lista.append(calculo)
            elif t == tamanho:
                lista.append(valores[tamanho])
            elif t > 0 < tamanho:
                calculo = int(valores[t]) + int(valores[len(valores)- (1 + t)]) 
                lista.append(calculo)
    else:
        for valor in range(int(len(valores)/2)):
            if valor > 0:
                calculo = int(valores[valor]) + int(valores[len(valores)- (1 + valor)]) 
                lista.append(calculo)
            elif valor == 0:
                calculo = int(valores[valor]) + int(valores[len(valores)- 1]) 
                lista.append(calculo)
    return lista

assert soma_simetricos([2, 5, 3, 9]) == [11, 8]
assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]


