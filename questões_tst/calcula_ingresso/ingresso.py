# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021
# EXERCÍCIO: PROGRAMA QUE LÊ NUMERO DE ADULTOS, CRIANÇAS E O PREÇO DO INGRESSO, E IMPRIME O VALOR TOTAL A SER PAGO

#|ENTRADAS|
adultos = int(input())
criancas = int(input())
preco_ingresso = float(input())

#|CALCULOS|
valor_adultos = preco_ingresso * adultos
valor_criancas = (criancas / 2) * preco_ingresso
valor_total = valor_adultos + valor_criancas

#|SAIDA|
print(f"Total: R$ {valor_total:.2f}")
