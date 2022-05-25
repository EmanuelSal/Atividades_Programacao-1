from simetricos import soma_simetricos
# testes para a funcao:

def test_1():
    assert soma_simetricos([2, 5, 3, 9]) == [11, 8]


def test_2():
    assert soma_simetricos([2, 5, 3, 9, 4]) == [6, 14, 3]


def test_3():
    assert soma_simetricos([3, 8, 5, 10, 9]) == [12, 18, 5]


def test_4():
    assert soma_simetricos([8, 2, 2, 8]) == [16, 4]


def test_5():
    assert soma_simetricos([8, 2]) == [10]


def test_5():
    assert soma_simetricos([8]) == [8]
