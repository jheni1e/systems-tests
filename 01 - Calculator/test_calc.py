from calc import soma, sub, mult, div

def test_somar():
    assert soma(3, 2) == 5
    
def test_subtrair():
    assert sub(5,2) == 3

def test_multiplicar():
    assert mult(3, 5) == 15

def test_dividir():
    assert div(20, 4) == 5
    assert div(10, 0) == "erro"