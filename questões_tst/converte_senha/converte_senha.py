palavra = input()
palavra2 = list(palavra)

trocas = 0
mensagem = ""

for i in range(len(palavra2)):
    if i > 0 and palavra2[i] == "a" or i > 0 and palavra2[i] == "A":
        palavra2[i] = "4"
        trocas += 1
    elif i > 0 and palavra2[i] == "e" or i > 0 and palavra2[i] == "E":
        palavra2[i] = "3"
        trocas += 1
    elif i > 0 and palavra2[i] == "i" or i > 0 and palavra2[i] == "I":
        palavra2[i] = "1"        
        trocas += 1
    elif i > 0 and palavra2[i] == "o" or i > 0 and palavra2[i] == "O":
        palavra2[i] = "0"
        trocas += 1

for letra in palavra2:
    mensagem += letra

print(f"{mensagem} ({trocas} troca(s))")