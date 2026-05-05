from calc import soma, sub, mult, div, min, odd, celtofah, fahtocel

def test_somar():
    assert soma(3, 2) == 5
    
def test_subtrair():
    assert sub(5,2) == 3

def test_multiplicar():
    assert mult(3, 5) == 15

def test_dividir():
    assert div(20, 4) == 5
    assert div(10, 0) == "erro"
    
def test_min():
    assert min(10, 2) == 2
    assert min(5, 12) == 5
    
def test_odd():
    assert odd(2) == True
    assert odd(3) == False
    
def test_celtofah():
    assert celtofah(50) == 122
    
def test_fahtocel():
    assert fahtocel(50) == 10