# coding: utf -8
# PROG1 - UGCG 
# ALUNO: EMANUEL VINICIUS | DATA: 15/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE VERIFICA SE O TRINÂNGULO É VALIDO OU NÃO

#|ENTRADAS| A, B, C - EM INTEIRO
a = int(input())
b = int(input())
c = int(input())

#|PROCESSAMENTO| CALCULO DAS ENTRADAS 
perimetro = a + b + c

if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b) < c < (a + b):
            classificacao = f"triangulo valido. {perimetro}"
else:
    classificacao = "triangulo invalido."

#|SAIDA| CLASSIFICAÇÃO DO TRIANGULO - VÁLIDO OU INVÁLIDO.
print(classificacao)