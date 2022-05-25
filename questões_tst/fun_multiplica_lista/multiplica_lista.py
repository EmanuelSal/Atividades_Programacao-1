def multiplica_lista(n, lista):

    if n > 0:
        lista2 = n * lista
    else:
        lista2 = []

    return lista2

l = ["joao", "pedro"]
l2 = ["21", "30", "44"]

assert multiplica_lista(2, l) == ["joao", "pedro", "joao", "pedro"]
assert multiplica_lista(2, l2) == ["21", "30", "44", "21", "30", "44"]
assert multiplica_lista(0, l2) == []
