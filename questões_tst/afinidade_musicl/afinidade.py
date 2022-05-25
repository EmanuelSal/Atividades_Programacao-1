def tem_afinidade(l1, l2):
    iguais = 0
    afinidade = False

    if len(l1) > len(l2):
        for i in range(len(l1)):
            for n in range(len(l2)):
                if l1[i] == l2[n]:
                    iguais += 1

    if iguais > 2:
        afinidade = True

    else:
        len(l2) >= len(l1):
            for i in range(len(l2)):
                for n in range(len(l1)):
                    if l2[i] == l1[n]:
                        iguais += 1

        if  iguais > 2:
            afinidade = True

    return afinidade

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
l3 = ['emanuel', 'junior', 'pedro', 'u2', 'leonardo']
l4 = ['junior', 'pedro', 'leonardo', 'lima']

assert tem_afinidade(l3, l4) == True
assert tem_afinidade(l1, l2) == True
assert tem_afinidade(l3, l2) == False
