from numpy import recarray


def rotesq(array):
    for i in range(len(array)):
        array[0] = array[-1]
        array[i + 1], array[i] = array[i], array[i + 1]
    return array
    
valores = [10, 20, 14, 17, 22, 9, 32]
rotesq(valores)
assert valores == [20, 14, 17, 22, 9, 32, 10]