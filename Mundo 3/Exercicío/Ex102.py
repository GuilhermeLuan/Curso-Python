'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def factorial(n, show=False):
    '''
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
    return f
    
print(factorial(5))
print(30*'=')
print(factorial(5, True))
