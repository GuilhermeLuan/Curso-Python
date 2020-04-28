'''
Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from time import sleep
from random import randint
numeros = []
temp = []

print(30*'-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30*'-')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(10*'-', f'{f"Sorteando {jogos} jogos":^5}', 10*'-')
for c in range(1, jogos+1):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    numeros.append(temp[:])
    temp.clear()
for i, l in enumerate(numeros):
    print(f'Jogos {i + 1}: {l}')
    sleep(0.2)
