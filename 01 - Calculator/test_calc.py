from calc import soma, sub, mult, div, min, even, celtofah, fahtocel, square, triangle, ellipse, metertocm, cmtometer, litertoml, mltoliter, dollartoreal, realtodollar

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
    
def test_metertocm():
    assert metertocm(1.2) == 120
    assert metertocm(3.5) == 350
    
def test_cmtometer():
    assert cmtometer(150) == 1.5
    assert cmtometer(300) == 3
    
def test_litertoml():
    assert litertoml(3) == 3000
    assert litertoml(2.3) == 2300
    
def test_mltoliter():
    assert mltoliter(3500) == 3.5
    assert mltoliter(4100) == 4.1
    
def test_dollartoreal():
    assert dollartoreal(5) == 24.5
    assert dollartoreal(10) == 49
    
def test_realtodollar():
    assert realtodollar(49) == 10
    assert realtodollar(98) == 20