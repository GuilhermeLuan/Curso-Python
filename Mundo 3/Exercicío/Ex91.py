'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

jogador = {}

print('Valores sorteados: ')

for j in range(1, 5):
    dado = randint(1, 6)
    jogador[f'jogador{j}'] = dado    

for k, v in jogador.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.4)
print(25*'-=')
print("  == RANKING DOS JOGADORES ==  ")

sorted_jogador = sorted(jogador.items(), key=lambda x: x[1], reverse=True) 
cont = 0
for k, i in sorted_jogador:
    cont += 1
    print(f' {cont} lugar para: {k} com {i}  ')
    sleep(0.4)
