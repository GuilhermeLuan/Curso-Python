# Exercício Python 108
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


def dobro(v=0):
    res = v * 2
    return res


def metade(v=0):
    res = v / 2
    return res


def aumentar(v=0, taxa=0):
    res = v + (v * taxa/100)
    return res


def diminuir(v=0, taxa=0):
    res = v - (v * taxa/100)
    return res


def formatacao(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
