# Exercício Python 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


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
