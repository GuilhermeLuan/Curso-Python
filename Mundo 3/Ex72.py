#Exercício Python 072
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 
'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num > 20:
        print('Tente novamente. ',end='')
        num = 0
        num = int(input("Digite um número entre 0 e 20: "))
        print(f'Você digitou o número {numero[num]}')
    else:
        print(f'Você digitou o número {numero[num]}')
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar ? [S/N]')).strip().upper()[0]
        if continuar in 'Nn':
            quit()