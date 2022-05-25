# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRICULA: 120210785
# EXERCÍCIO: PROGRAMA QUE CALCULE O CUSTO DO SERVIÇO DO PINTOR

#|ENTRADAS|
altura = float(input())
largura = float(input())

#|CALCULOS|
area = altura * largura
metro = 20.00
custo = area * metro

#|SAIDA|
print(f"R$ {custo:.2f}")
