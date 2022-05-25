vendedor = input("Qual é o nome do(a) vendedor(a)? ")
valor = float(input("Qual é o valor da venda? "))

if valor <= 500.00:
    comissao = valor * 0.05
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor} é R$ {comissao:.2f}.")
else:
    comissao = valor * 0.10
    print(f"O valor da comissão para o(a) vendedor(a) {vendedor[:5]} é R$ {comissao:.2f}.")

