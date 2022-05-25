# PROGRAMAÇÃO 1 - UFCG
# ALUNO: EMANUEL VINICIUS | MATRICULA: 120210785
# DATA: 24/02/2022
# QUESTÃO: EQUIPES - DIZER QUAIS AS MODALIDADES PARA A QUANTIDADE DE NOMES DA ENTRADA

#entradas:

jogadores = []
modalidade = "Equipe Inválida"
while True:
    nomes = input()
    if nomes == "-": break

    elif nomes != "-":
        jogadores.append(nomes)
        time = len(jogadores)
#saidas:
if time == 11:
    modalidade = "Futebol"
    print(f"Modalidade -> {modalidade}")

elif time == 6:
    modalidade = "Vôlei"
    print(f"Modalidade -> {modalidade}")

elif time == 5:
    modalidade = "Basquete"
    print(f"Modalidade -> {modalidade}")

elif time == 7:
    modalidade = "Handebol"
    print(f"Modalidade -> {modalidade}")

else:
    print(modalidade)