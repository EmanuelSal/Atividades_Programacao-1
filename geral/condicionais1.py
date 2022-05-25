# PROG1 - UFCG
# EMANUEL VINICIUS SÁ DE LIMA E LIMA - MATRPICULA: 120210785
# EXERCÍCIO: MOSTRAR O RESULTADO DE UM JOGO DE FUTEBOL


gols_time_a = int(input())
gols_time_b = int(input())

resultado = None

if gols_time_a > gols_time_b:
    resultado = "TIME A VENCEDOR!!"

elif gols_time_b > gols_time_a:
    resultado = "TIME B VENCEDOR!!"

else:
    resultado = "EMPATE!"

print(resultado)
