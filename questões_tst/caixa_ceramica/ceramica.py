# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA : 14/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE CALCULE A QUANTIDADE DE CAIXAS DE CERAMICA NECESSÁRIAS PARA COBRIR O AMBIENTE

#|ENTRADAS|
capacidade = float(input("Capacidade de revestimento? "))

print("\n== Dados do vão a revestir ==")

a = float(input("Comprimento? "))
b = float(input("Largura? "))
c = float(input("Altura? "))

#|CALCULOS|
area = (2 * (a*b) + 2 * (a*c) + 2 * (b*c)) - (a*b)
numero_caixas = int(area / capacidade)

#|SAIDA|

print('\n== Resultados ==')
print(f"Área total a revestir: {area:.1f} m2")
print(f"Número de caixas: {numero_caixas:}")
