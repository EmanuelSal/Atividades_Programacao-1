# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE CALCULA A QUANTIDADE DE CAMPOS E SUA MEDIA

#|ENTRADAS|
area1 = float(input())
area2 = float(input())
area3 = float(input())

#|CALCULOS|
campo = 4000.0
campo1 = area1 / campo
campo2 = area2 / campo
campo3 = area3 / campo
media = (campo1 + campo2 + campo3) / 3

#|SAIDA|
print(f"{campo1:.2f}")
print(f"{campo2:.2f}")
print(f"{campo3:.2f}")
print(f"{media:.2f}")
