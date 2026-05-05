from calc import soma, sub, mult, div, min, even, celtofah, fahtocel, square, triangle, ellipse

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
    
def test_even():
    assert even(2) == True
    assert even(3) == False
    
def test_celtofah():
    assert celtofah(50) == 122
    
def test_fahtocel():
    assert fahtocel(50) == 10
    
def test_square():
    assert square(3, 15) == 45
    assert square(2, 4) == 8
    
def test_triangle():
    assert triangle(5, 3) == 7.5
    assert triangle(4, 6) == 12
    
def test_ellipse():
    assert ellipse(3, 4) == 37.68
    assert ellipse(2, 7) == 43.96