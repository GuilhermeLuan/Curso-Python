'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(l, c):
    soma = l * c
    print(f'A área de um terro {l:.1f}x{c:.1f} é de {soma:.1f}m².')



# Programa principal
print('Controle de Terrenos')
print(20*'-')
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (M): '))
área(larg, comp)
