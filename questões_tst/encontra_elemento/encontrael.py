numero = input()
sequencia = input().split()




for valor in sequencia:
    if valor == numero:
        print("sim")
        break

if valor != numero:
    print("não")