'''
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from time import sleep
from random import randint
jogos = []
temp = []

print(30*'-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30*'-')

num = int(input('Quantos jogos você quer que eu sorteie? '))

print(10*'-', f'{f"Sorteando {num} jogos":^5}', 10*'-')

for a in range(1, num + 1):
    for c in range(1, 7):
        n = randint(1, 60)
        temp.append(n)
    jogos.append(temp[:])
    temp.clear()
cont = 0
for nu in range(0, num):
    cont += 1
    print(f'Jogo {cont}: {jogos[nu]}')