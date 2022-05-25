# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 16/12/2021  
# MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE LÊ A CAPACIDADE MÁXIMA QUE UM ELEVADOR PODE TRANSPORTAR E O PESO MÉDIO DAS PESSOAS

#|ENTRADAS| 2 VALORES INTEIROS - CAPACIDADE DO ELEVADOR E PESO
capacidade = int(input())
peso = int(input())

#|CÁLCULOS|
quantidade_elevador = capacidade // peso

#|SAÍDA| PROMPT COM A QUANTIDADE DE PESSOAS
print(f"O elevador pode transportar {quantidade_elevador} pessoas com segurança.")
