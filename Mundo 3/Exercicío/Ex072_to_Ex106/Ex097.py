'''
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
'''
def escreva(frase):
    tamanho = len(frase) + 6
    print(tamanho * '~')
    print(f'{frase.center(tamanho)}')
    print(tamanho * '~')


# Programa Principal
escreva(str(input('Escreva uma mensagem: ')))
