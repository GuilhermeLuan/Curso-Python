import random
from time import sleep
lista = ['Papel','Tesoura','Pedra']
computador = random.choice(lista)
print('Pedra, Papel e Tesoura')
opcao = str(input("Suas opções:"
                  "\n PEDRA"
                  "\n PAPEL"
                  "\n TESOURA"
                  "\n Qual é sua jogada? ").lower())

print('JO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO!!!')
sleep(0.3)

#CONDIÇÃO SE JOGADOR JOGAR PEDRA
if opcao == 'pedra' and computador == 'Tesoura':
    print(10*'-=')
    print('Computador jogou {} \nJogador Jogou Pedra'.format(computador))
    print(10 * '-=')
    print('JOGADOR VENCEU')
elif opcao == 'pedra' and computador == 'Papel':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Pedra'.format(computador))
    print(10 * '-=')
    print('COMPUTADOR VENCEU')
elif opcao == 'pedra' and computador == 'Pedra':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Pedra'.format(computador))
    print(10 * '-=')
    print('EMPATE')
#CONDIÇÃO SE JOGADOR JOGAR PAPEL
if opcao == 'papel' and computador == 'Pedra':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Papel'.format(computador))
    print(10 * '-=')
    print('JOGADOR VENCEU')
elif opcao == 'papel' and computador == 'Tesoura':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Papel'.format(computador))
    print(10 * '-=')
    print('COMPUTADOR VENCEU')
elif opcao == 'papel' and computador == 'Papel':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Papel'.format(computador))
    print(10 * '-=')
    print('EMPATE')
#CONDIÇÃO SE JOGADOR JOGAR TESOURA
if opcao == 'tesoura' and computador == 'Papel':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Tesoura'.format(computador))
    print(10 * '-=')
    print('JOGADOR VENCEU')
elif opcao == 'tesoura' and computador == 'Pedra':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Tesoura'.format(computador))
    print(10 * '-=')
    print('COMPUTADOR VENCEU')
elif opcao == 'tesoura' and computador == 'Tesoura':
    print(10 * '-=')
    print('Computador jogou {} \nJogador Jogou Tesoura'.format(computador))
    print(10 * '-=')
    print('EMPATE!')

