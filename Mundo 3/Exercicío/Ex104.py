'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(num=''):
    global n
    n = ''
    pergunta = input(num)
    pergunta.strip()

    n = pergunta
    if pergunta.isnumeric() == False:
        print('ERRO! Digite um número inteiro válido.')
        while pergunta.isnumeric() == False:
            return input(num)
        

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
