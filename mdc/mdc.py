a = int(input())
b = int(input())

maior = 0
menor = 0
resto = 0

while True:
    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    resto = maior % menor


    print(f'maior: {maior}')
    print(f'menor: {menor}')
    print(f'resto: {resto}')
    print(f'------')

    print(f"MDC: {resto}")
    if resto ==0: break

