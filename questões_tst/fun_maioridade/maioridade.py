def maioridade_penal(nomes, idades):

    nome = nomes.split()
    idade = idades.split()
    maiores = []
    saida = ""

    for n in range(len(nome)):
        if int(idade[n]) >= 18:
            maiores.append(nome[n])

    for i in range(len(maiores)):
        if i == len(maiores) -1:
            saida += f"{maiores[i]}"

        else:
            saida += f"{maiores[i]} "

    return saida

assert maioridade_penal("Jansen Italo Ana", "14 21 60") == "Italo Ana"
