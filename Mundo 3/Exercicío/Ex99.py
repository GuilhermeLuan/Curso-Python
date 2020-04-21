'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*num):
    print(20*'-=')
    print('Analisando os valores passados...')

    for n in num:
        print(f'{n}',end=' ')

    print(f'Foram informados {len(num)} ao todo.')

    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}')
    else:
        m = 0
        print(f'O maior valor informado foi {m}')
    print(20*'-=')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
