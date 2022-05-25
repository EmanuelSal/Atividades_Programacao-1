# primeira linha da entrada determina a posição do jogador, dois valores inteiros separados por espaços
# linha e coluna respectivamente

posicao_inicial = input().split()
coluna = int(posicao_inicial[0])
linha = int(posicao_inicial[1])

total = 0
while True:
    posicoes = input()
    comandos = posicoes.split()
    if posicoes == "X": break
    lados = comandos[0]
    valor = int(comandos[1])
    if lados == "C":
        linha = linha - valor
    if lados == "B":
        linha = linha + valor
    if lados == "D":
        coluna = coluna + valor
    if lados == "E":
        coluna = coluna - valor
    
    total += valor
    print(f"> {linha} {coluna}")

print(total)