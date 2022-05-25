from p1 import Array


_steps = 0

def booblesort(a):
    global _steps
    for j in range(len(a)):
        houve = False
        for i in range(len(a) -1 -j):
            _steps += 1
            if a[i] > a[i + 1]:
                temp =a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                houve = True

        if not houve: return

def bs(a):
    for j in range(len(a) -1):
        for i in range(len(a) -1):
            if a[i] > a[i+1]:
                a[i], a[i + 1] = a[i + 1], a[i]

a = Array(8)
a[0] = 50
a[1] = 40
a[2] = 30
a[3] = 90
a[4] = 10
a[5] = 80
a[6] = 70
a[7] = 60

print(a)
bs(a)
print(a)

