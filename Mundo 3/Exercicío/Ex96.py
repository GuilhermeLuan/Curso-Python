'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
'''
def área(x, y):
    soma = x * y
    print(f'A área de um terro {x:.1f}x{y:.1f} é de {soma:.1f}m².')



# Programa principal
print('Controle de Terrenos')
print(20*'-')
x = float(input('Largura (m): '))
y = float(input('Comprimento (M): '))
área(x, y)
