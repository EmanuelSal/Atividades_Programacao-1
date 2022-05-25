from p1 import Array

def insere(a, index, valor):
    for i in range(len(a) -1, index, -1):
        a[i] = a[i - 1]
    a[index] = valor

def insere_ordenado(a, num):
    assert a[len(a) -1] is not None, "Array cheio"

    for i in range(len(a)):
        if a[i] is None: break
        if num <= a[i]:
            insere(a, i, num)
            return

    # Ou o Array ta cheio ou chegamos em um None
    a[i] = num


a = Array(10)

while True:
    linha = input()
    if not linha: break
    num = int(linha)
    insere_ordenado(a, num)
    print(a)

print("tchau")
