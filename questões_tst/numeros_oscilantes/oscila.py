codigo = input()

quantidade = len(codigo)

saida =''

for numero in range(len(codigo) - 1):
    
    atual = int(codigo[numero])
    proximo = int(codigo[numero + 1])
    
    if  atual % 2 == 0 and proximo % 2 != 0:
        saida = f"verdadeiro: {quantidade} algarismos."
    
    elif atual % 2 != 0 and proximo % 2 == 0:
        saida = f"verdadeiro: {quantidade} algarismos."
    
    elif atual % 2 == 0 and proximo % 2 == 0:
        saida = f"falso: {quantidade} algarismos."
        break
    elif atual % 2 != 0 and proximo % 2 != 0:
        saida = f"falso: {quantidade} algarismos."
        break
    

print(saida)