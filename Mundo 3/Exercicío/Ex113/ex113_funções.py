"""
Exercício Python 113:
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        try:
            valor = int(n)
            ok = True
        except ValueError:
            print('ERRO! Digite um número inteiro válido')
        if ok:
            break
    return valor


def leiaFloat(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        try:
            valor = float(n)
            ok = True
        except ValueError:
            print('ERRO! Digite um número real válido')
        if ok:
            break
    return valor