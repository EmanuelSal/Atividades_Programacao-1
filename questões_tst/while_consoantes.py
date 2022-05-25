def sentinela(palavra):
    consoantes = 0
    vogais = 0
    for letra in palavra:
        if letra.lower() in "aeiou": vogais += 1
        else: consoantes += 1
    return consoantes > vogais

count = 0
while True:
    dado = input()
    count += 1
    if sentinela(dado): break

print(count)