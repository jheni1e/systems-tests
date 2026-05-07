from login import autenticar

def login_valido():
    assert autenticar('jhenie', 'jhenie123')

def login_usuario_invalido():
    assert autenticar('jhenifer', 'jhenie123')

def login_senha_invalida():
    assert autenticar('jhenie', 'jhenie123456')

def login_ambos_invalidos():
    assert autenticar('jhenifer', 'jhenifer123')