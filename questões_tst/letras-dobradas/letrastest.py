def palavras_dobradas(palavra):
    for i in range(len(palavra) - 1):
        if palavra[i] == palavra[i + 1]:
            return True
    return False


n = int(input())

palavras= []
dobradas= []
nao_dobradas= []

for c in range(n):
    palavra= input()
    palavras.append(palavra)
for palavra in palavras:
    if palavras_dobradas(palavra) == True:
        dobradas.append(palavra)
    else:
        nao_dobradas.append(palavra)

print(f'{len(dobradas)} palavra(s) com letras dobradas:')

for palavra in dobradas:
    print(palavra)

print('---')

print(f'{len(nao_dobradas)} palavra(s) sem letras dobradas:')

for palavra in nao_dobradas:
    print(palavra)