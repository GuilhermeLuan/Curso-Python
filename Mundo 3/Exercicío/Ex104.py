'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''

def leiaInt(num=''):
    global n
    n = ''
    pergunta = input(num).strip()
    n = pergunta

    while n.isnumeric() == False:
        print('ERRO! Digite um número inteiro válido.')
        validação = input(num).strip()
        if validação.isnumeric() == True:
            return validação
    else:
        return n

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número: {n}')
