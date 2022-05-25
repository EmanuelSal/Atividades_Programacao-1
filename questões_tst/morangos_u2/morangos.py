# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 16/12/2021  
# MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE LÊ A QUANTIDADE DE MORANGOS E IMPRIMA QUANTAS CAIXAS SERÃO COMPLETAMENTE PREENCHIDAS

#|ENTRADAS| EM INTEIRO - REFERENTE A QUANTIDADE DE MORANGOS
morangos = int(input())

#|CALCULOS|
caixa = 400
caixas_cheias = morangos // caixa
porcentagem = ((morangos % caixa) * 100) / morangos

#|SAIDA|
print(f"{caixas_cheias} caixa(s) completa(s) para embalar os morangos.")
print(f"{porcentagem:.1f}% dos morangos serão perdidos.")

