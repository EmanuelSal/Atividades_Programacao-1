num = int(input("DIGITE UM NÚMERO: "))

for i in range(1, 11):
    conta = num * i
    print(f"{num} x {i} = {conta}")

print("=" * 10)
print("FIM DA TABUADA!")

pergunta = input("Deseja mais algum número? ")
if pergunta == "nao":
    print("Ok, Tchau!")
else:
    sec_num = int(input("Qual o próximo número? "))
    for n in range(1, 11):
        conta = sec_num * n
        print(f"{sec_num} x {n} = {conta}")
    print("=" * 10)
    print("FIM DA TABUADA!")
