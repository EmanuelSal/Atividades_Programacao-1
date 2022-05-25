# PROGRAMAÇÃO 1 - UFCG - REPOSIÇÃO
# MATRICULA: 120210785 | DATA: 30/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE FILTRE AS ENTRADAS E DIGA QUAIS ENTRADAS SÃO INVALIDAS

# contadores para linhas e sequencias invalidas
saida = "" 
count_linhas = 0
sequencias_invalidas = 0
while True:
    entradas = input()
    entrada = entradas.split()
    # contador de números pares e impares
    num_pares = 0
    num_impares = 0

    # Sentinela | condicao de parada do laco
    if entradas == "fim": break
    count_linhas += 1 # contador para cada entrada lida após o break, para que o sentinela não entre nessa contagem
    
    for i in range(len(entrada)):
        if int(entrada[i]) % 2 == 0:
           num_pares += 1
        else:
            num_impares += 1
    
    # condicao para que seja indicada a linha que está invalida e a sequencia:
    if num_pares < num_impares:
        sequencias_invalidas += 1
        saida = f"linha {count_linhas} inválida: {entradas}"
        print(saida)
    

print(f"sequências lidas: {count_linhas} (inválidas: {sequencias_invalidas})")

