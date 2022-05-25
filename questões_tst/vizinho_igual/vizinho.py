entrada = input().split()

repeticoes = 0
for elemento in range(len(entrada) -1):
    if entrada[elemento] == entrada[elemento + 1]:
        repeticoes += 1

print(repeticoes)