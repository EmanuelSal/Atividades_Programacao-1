# PROG1 - UFCG
# EMANUEL VINICIUS SÁ DE LIMA E LIMA - MATRPICULA: 120210785
# EXERCÍCIO: classificar de acorco com a idade

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

mensagem = None

#SE FOR IDOSO...
if idade >= 60:
    mensagem = f"{nome}, você se classifica como idoso!"

#SE NÃO FOR IDOSO...
elif idade >= 18:
    mensagem = f"{nome}, você se classifica como adulto!"

#SE NÃO FOR ADULTO...
elif idade >= 12:
    mensagem = f"{nome}, você se classifica como adolescente!"

#SE NÃO FOR NENHUM DOS CASOS... SERÁ CRIANÇA
else:
    mensagem = f"{nome}, você se classifica como criança!"

print(mensagem)