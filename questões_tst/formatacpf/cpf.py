# coding: utf -8
# PROG1 - UGCG 
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE IMPRIME A SOMA DOS DOIS ULTIMOS DIGITOS DOS CPFs LIDOS

#|ENTRADAS| 3 ENTRADAS - EM INTEIRO
cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

#|CALCULOS| CALCULO DOS ULTIMOS DOIS DIGITOS E MANIPULAÇÃO DAS ENTRADAS

# Para o cpf1:
cpf1_inteiro = cpf1 // 100
resto_cpf1 = cpf1 % 100
inteiro_resto_cpf1 = resto_cpf1 // 10
resto_resto_cpf1 = resto_cpf1 % 10
soma_digitos_cpf1 = inteiro_resto_cpf1 + resto_resto_cpf1

# Para o cpf2:
cpf2_inteiro = cpf2 // 100
resto_cpf2 = cpf2 % 100
inteiro_resto_cpf2 = resto_cpf2 // 10
resto_resto_cpf2 = resto_cpf2 % 10
soma_digitos_cpf2 = inteiro_resto_cpf2 + resto_resto_cpf2

# Para o cpf3:
cpf3_inteiro = cpf3 // 100
resto_cpf3 = cpf3 % 100
inteiro_resto_cpf3 = resto_cpf3 // 10
resto_resto_cpf3 = resto_cpf3 % 10
soma_digitos_cpf3 = inteiro_resto_cpf3 + resto_resto_cpf3

#|SAIDA| SEM PROMPTS
print(f"{cpf1_inteiro}-{resto_cpf1}")
print(f"{soma_digitos_cpf1}")
print(f"{cpf2_inteiro}-{resto_cpf2}")
print(f"{soma_digitos_cpf2}")
print(f"{cpf3_inteiro}-{resto_cpf3}")
print(f"{soma_digitos_cpf3}")
