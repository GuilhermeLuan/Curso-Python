# Exercício Python 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {price} é R${moeda.metade(price)}')
print(f'O dobro de R${price} é R${moeda.dobro(price)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(price, 10)}')
