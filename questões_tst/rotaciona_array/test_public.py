from undertst import rotesq

def test_exemplo():
    valores = [10, 20, 14, 17, 22, 9, 32]
    rotesq(valores)
    assert valores == [20, 14, 17, 22, 9, 32, 10]
