# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE CALCULA A SUPERFICIE DE UM CILINDRO

import math

#|ENTRADA| MEDIDAS EM FLOATS
print("Cálculo da Superfície de um Cilindro\n---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

#|CALCULO| 
raio = diametro / 2
area_lateral = 2 * math.pi * raio * altura
area_base = math.pi * (raio ** 2)
area_total = area_lateral + (2 * area_base)

#|SAIDA|
print("---")
print(f"Área calculada: {area_total:.2f}")
