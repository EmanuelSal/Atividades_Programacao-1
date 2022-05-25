# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 16/12/2021  
# MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE DETECTA PERTURBAÇÃO

#|ENTRADAS|
ruido = input()
hora = int(input())

#|PROCESSAMENTO|

if ruido != "" and hora > 22:
    mensagem = "Perturbação Detectada!"
else:
    mensagem = "Condomínio em Paz."

print(mensagem)
