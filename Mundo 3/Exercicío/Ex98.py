'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
def contador(início, fim, passo):
    print(30*'-')
    print(f'Contagem de {início} ate {fim} de {passo} em {passo}')
    passo = abs(passo) if passo != 0 else 1

    if início < fim:
        for n in range(início, fim + 1, passo):
            print(n, end=' ')
            
    if início > fim:
        for n in range(início, fim - 1, -passo):
            print(n, end=' ')
        
    print('FIM')
    print(30*'-')

contador(1, 10, 1)
contador(10, 0, -2)

contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
