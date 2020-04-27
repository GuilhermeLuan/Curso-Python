# Exercício Python 108
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


def dobro(v):
    res = v * 2
    return res


def metade(v):
    res = v / 2
    return res


def aumentar(v, taxa):
    res = v + (v * taxa/100)
    return res


def diminuir(v, taxa):
    res = v - (v * taxa/100)
    return res


def formatacao(v):
    valor = str(v).replace('.', ',')
    res = f'R${valor}'
    return res
