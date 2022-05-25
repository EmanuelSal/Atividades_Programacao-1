seq = input().split()
dado = input()

variavel = False
for e in seq:
    if e == dado:
        variavel = True

if variavel:
    print("Tem")
else:
    print("Não tem")





