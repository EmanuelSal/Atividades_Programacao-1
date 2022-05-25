# coding: utf -8
# PROG1 - UGCG 
# ALUNO: EMANUEL VINICIUS | DATA: 15/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE DETERMINA EM QUE CATEGORIA UM NADADOR IRA COMPETIR BASEADO NA IDADE

#|ENTRADAS| NOME (EM STRINGS) - IDADE (EM INTEIROS)
nome = input()
idade = int(input())

#|PROCESSAMENTO| CONDIÇÕES PARA AS IDADES E CLASSIFICAÇÕES
if 5 <= idade <= 7:
    classificacao = f"{nome}, {idade} anos, Infantil A."
elif 8 <= idade <= 10:
    classificacao = f"{nome}, {idade} anos, Infantil B."
elif 11 <= idade <= 13:
    classificacao = f"{nome}, {idade} anos, Juvenil A."
elif 14 <= idade <= 17:
    classificacao = f"{nome}, {idade} anos, Juvenil B."
elif idade > 17:
    classificacao = f"{nome}, {idade} anos, Senior."
else:
    classificacao = f"{nome}, {idade} anos, Não pode competir."

#|SAIDA| IMPRIMINDO OS NOMES, ANOS E CLASSIFICAÇÕES
print(classificacao)