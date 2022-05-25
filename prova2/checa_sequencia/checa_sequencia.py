# PROGRAMAÇÃO 1 - UFCG - PROVA 2
# Matricula: 120210785 | Data: 21/03/2022
# Aluno: Emanuel Vinicius Sá de Lima e Lima
# Questão: Questão que checa a sequencia de digitos e "para", de acordo com as condições de paradas dadas.



# Entradas:
impares = 0
nums_lidos = 0
soma = 0 


saida = ""
while True:
    sequencia = input()
    limite = int(input())
    total_nums = len(sequencia)
    
    # Checando cada indice da entrada (sequencia):
    indice = 0
    while indice < total_nums:
        nums_lidos += 1 # quandidade de numeros lidos até agora
        soma += int(sequencia[indice]) # Soma de cada valor da sequencia
        
        # Primeira condição: se o número for impar e atingir a quantidade 6 (criterio)
        if int(sequencia[indice]) % 2 != 0:
            impares += 1
            if impares == 6: 
                saida = f"{impares} ímpares" # alterando a variavel de saida de acordo com a condição
                break
                
        # Segunda condição: se a soma for maior ou igual ao valor limite: sai do segundo laço
        if soma >= limite: 
            saida = "limite"
            break
       
        # Terceira condição: se todos os números da sequencia forem lidos 
        if nums_lidos == total_nums: 
            saida = "final da sequência"
            break   
    
        indice += 1
    
    # Condições para sair do primeiro laço
    if impares == 6: break

    elif soma >= limite: break

    elif nums_lidos == total_nums: break

# Saídas:
print(f"soma: {soma}")
print(f"números lidos: {nums_lidos} de {total_nums}")
print(f"critério de parada: {saida}")
