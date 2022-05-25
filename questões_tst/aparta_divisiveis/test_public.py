from undertst import aparta

def test_do_enunciado():
    v = [8, 10, 11, 7, 21, 2, 17, 6, 28, 24]
    assert aparta(v, 3) == 3
    assert v == [8, 10, 11, 7, 2, 17, 28, 21, 6, 24]
