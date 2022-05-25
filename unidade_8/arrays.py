from random import randint
from p1 import Array
from random import randint

def insere(a, index, valor):
    for i in range(len(a) -1, index, -1):
        a[i] = a[i-1]
    a[index] = valor


def pop(a, index):
    for i in range(index, len(a) -1):
        a[i] = a[i +1]
    a[len(a) -1] = None

def main():
    a = Array(5)
    for i in range(len(a) -1):
        a[i] = randint(0, len(a) -1)
    
    print(a)
    insere(a, 3, 100)
    print(a)
    pop(a, 3)
    pop(a, 3)
    pop(a, 3)
    print(a)

if __name__ == "__main__":
    main()
