# coding: utf -8
# PROG1 - UGCG 
# ALUNO: EMANUEL VINICIUS | DATA: 16/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE IMPRIME EM ORDEM CRESCENTE OS INTEIROS

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n2 > n1:
    aux = n1
    n1 = n2
    n2 = aux
if n3 > n1:
    aux = n1
    n1 = n3
    n3 = aux
if n3 > n2:
    aux = n2
    n2 = n3
    n3 = aux

print(f"{n3} {n2} {n1}")
