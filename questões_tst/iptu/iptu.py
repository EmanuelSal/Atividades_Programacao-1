# coding: utf -8
# PROG1 - UFCG
# ALUNO: EMANUEL VINICIUS | DATA: 14/12/2021 | MATRICULA: 120210785
# EXERCICIO: PROGRAMA QUE CALCULE O VALOR DO IPTU E AS ALTERNATIVAS DE PAGAMENTO.

#|ENTRADAS| COM PROMPTS E EM FLOATS
area = float(input("Área construída? "))
aliquota = float(input("Alíquota? "))

#|CALCULOS| VALOR DO IPTU E SUAS FORMAS DE PAGAMENTO
iptu = (area * aliquota) + 35.00
quota_unica = iptu - (iptu  * 0.25)
parcelas6 = iptu - (iptu * 0.05)
valor_6parcelas = parcelas6 / 6
parcelas10 = iptu / 10

#|SAIDA|
print(f"IPTU: R$ {iptu:.2f}")
print()
print("Pagamento:")
print(f"1. Quota única. R$ {quota_unica:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {parcelas6:.2f}\n   6 x R$ {valor_6parcelas:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {iptu:.2f}\n   10 x R$ {parcelas10:.2f}")
