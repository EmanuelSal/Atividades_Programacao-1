recorde_atual = float(input())
quantidade_comida = float(input())


if recorde_atual ==  quantidade_comida:
    print("recorde empatado")

elif quantidade_comida > recorde_atual:
    print(f"recorde quebrado ({quantidade_comida} kg)")

else:
     print("recorde mantido")


