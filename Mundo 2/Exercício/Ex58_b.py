#GERADOR DO NÚMERO
from random import randint
num = randint(0,10)
cont = 0
vidas = 4
print(num)
print('Sou seu computador...')
print('Acabei de pensar em um número entra 0 e 10.')
print('Será que você consegue adivinhar qual foi ? Você tem 5 vidas !')
n = int(input('Qual seu palpite ? '))
while n != num:
    if num > n:
        print('Mais... Tente mais uma vez.')
        n = int(input('Qual seu palpite? '))
        cont = cont + 1
        vidas = vidas - 1
    if num < n:
        print('Menos.. Tente mais uma vez. ')
        n = int(input('Qual seu palpite? '))
        cont = cont + 1
        vidas = vidas - 1
    if vidas == 0:
        print('Game Over ! Suas vidas acabaram, o computador pensou no número {}'.format(num))
    if num == n:
        print('Acertou com {} tentativas. Parabéns!'.format(cont))
