def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def min(x, y):
    if (x < y):
        return x
    else:
        return y
    
def even(x):
    return x % 2 == 0

def celtofah(c):
    return (c * 1.8) + 32
    
def fahtocel(f):
    return (f - 32) * 5/9

def square(w, h):
    return w * h

def triangle(a, b):
    return (a * b) /2

def ellipse(a, b):
    return 3.14 * a * b

def metertocm(m):
    return m * 100

def cmtometer(cm):
    return cm / 100

def litertoml(l):
    return l * 1000

def mltoliter(ml):
    return ml / 1000

def dollartoreal(d):
    return d * 4.9

def realtodollar(r):
    return r / 4.9