dic = {"A": 2, "B": 3, "C": 5, "D": 6}

for chave, valor in dic.items():
    print(chave, valor)

print("-" * 30)

count = 0
for valor in dic.values():
    count += valor

print(count)

