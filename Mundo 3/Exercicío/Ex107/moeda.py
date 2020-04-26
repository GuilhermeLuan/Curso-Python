# Exercício Python 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# def dobro(v):
#     dobro


def aumentar(v):
    aumentar = v + (v * v/100)
    print(f'Aumentando 10%, temos {aumentar}')
