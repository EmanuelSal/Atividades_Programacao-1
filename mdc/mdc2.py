num1 = int(input())
num2 = int(input())

dividendo = num1
divisor = num2
resto = dividendo % divisor

while resto != 0:
    dividendo = divisor
    divisor = resto
    resto = dividendo % divisor

    print(f"maior: {dividendo}\nmenor: {divisor}\nresto: {resto}\n----------")

    if resto == 0:
        print(f"maior: {divisor}\nmenor: {resto}\n----------\nMDC: {divisor}")

