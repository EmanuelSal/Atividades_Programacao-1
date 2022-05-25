# PROGRAMAÇÃO 1- UFCG
# MATRICULA: 120210785 | DATA: 09/03/2022
# ALUNO: EMANUEL VINICIUS SÁ DE LIMA E LIMA
# PROGRAMA QUE SOMA OS INTERVALOS ENTRE DOIS NÚMEROS


def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b + 1):
        if a <= b:
            soma += i

    return soma

assert soma_intervalo(5, 15) == 110
assert soma_intervalo(10, 10) == 10
assert soma_intervalo(3, 25) == 322
