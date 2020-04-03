from random import randint
pc = randint(0,10)
contador = 0
print('Sou um computador... \nAcabei de pensar em um número entre 0 e 10. \nSerá que você consegue adivinhar qual foi?')
palpite = int(input('Qual é o seu papalpite ?'))
contador = contador + 1

while True:
    if palpite != pc:
        if palpite < pc:
            print('Mais... Tente mais uma vez.')
            contador = contador + 1
        palpite = int(input('Qual é o seu papalpite ?'))
        if palpite > pc:
            print('Menos... Tente mais uma vez.') 
            contador = contador + 1
        palpite = int(input('Qual é o seu papalpite ?'))
    if palpite == pc:
        break
print(f'Acertou com {contador} tentativas. Parabéns')