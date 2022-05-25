#PROG1 - UFCG
#ALUNO; EMANUEL VINICIUS | MATRÍCULA: 120210785
#SIMULADO DATA: 03/02/2022
#PROGRAMA QUE IDENTIFIQUE LETRAS DOBRADAS


def dobradas(string):
    for i in range(len(string) -1):
        if string[i] == string[i + 1]:
            return True
    return False

numero_palavras = int(input())

todas = []
dobrada = []
nao_dobradas = []

for i in range(numero_palavras):
    palavra = input()
    todas.append(palavra)

for palavra in todas:
    if dobradas(palavra) == True:
        dobrada.append(palavra)
    else:
        nao_dobradas.append(palavra)


print(f"{len(dobrada)} palavra(s) com letras dobradas:")

for palavra1 in dobrada:
    print(palavra1)

print('---')
print(f"{len(nao_dobradas)} palavra(s) sem letras dobradas:")

for palavra2 in nao_dobradas:
    print(palavra2)




