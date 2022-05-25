# coding: utf -8
# PROG1 - UGCG 
# ALUNO: EMANUEL VINICIUS | DATA: 15/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE IMPRIMA O RESULTADO DA PARTIDA A PARTIR DO NÚMERO DE GOLS

#|ENTRADAS| NÚMERO DE GOLS - (EM INTEIRO)
gols_campinense = int(input())
gols_trezes = int(input())

#|PROCESSAMENTO| CONDIÇÕES PARA O RESULTADO DA PARTIDA
if gols_campinense > gols_trezes:
    resultado = "Campinense"
elif gols_trezes > gols_campinense:
    resultado = "Treze"
else:
    resultado = "Empate"

#|SAÍDA| RESULTADO DA PARTIDA A PARTIR DO NÚMERO DE GOLS
print(resultado) 