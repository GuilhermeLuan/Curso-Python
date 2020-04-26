# Exercício Python 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def dobro(v):
    return v * 2


def metade(v):
    return v / 2


def aumentar(v):
    return v + (v * 10/100)


def diminuir(v):
    return v - (v * 10/100)
