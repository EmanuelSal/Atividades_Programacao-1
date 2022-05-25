grau = int(input())

if 0 < grau < 90:
    mensagem = "Quadrante 1"
elif 90 < grau < 180:
    mensagem = "Quadrante 2"
elif 180 < grau < 270:
    mensagem = "Quadrante 3"
elif 270 < grau < 360:
    mensagem = "Quadrante 4"

if grau == 0 or grau == 90 or grau == 180 or grau == 270 or grau == 360:
    mensagem = "Sobre eixos"

if grau > 360:
    conta = grau % 360
    if 0 < conta < 90:
        mensagem = "Quadrante 1"
    elif 90 < conta < 180:
        mensagem = "Quadrante 2"
    elif 180 < conta < 270:
        mensagem = "Quadrante 3"
    elif 270 < conta < 360:
        mensagem = "Quadrante 4"
    else:
        mensagem = "Sobre eixos"

print(mensagem)
