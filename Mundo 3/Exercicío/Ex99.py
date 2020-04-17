'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
from random import randint

def maior(*num):
    temp = []
    temp.append(num)

    print(20*'-=')
    print('Analisando os valores passados...')

    for i, v in enumerate(temp[0]):
        print(f'{v}',end=' ')

    print(f'Foram informados {len(temp[0])} ao todo.')

    if len(temp[0]) > 0:
        print(f'O maior valor informado foi {max(temp[0])}')
    else:
        print('Não foi informado nenhum valor !')
    print(20*'-=')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
