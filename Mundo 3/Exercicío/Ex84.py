"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""
dado = []
galera = []
peso_lista = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    peso_lista.append(dado[1])
    galera.append(dado[:])
    dado.clear()
    continuar = str(input('Deseja continuar ? [S/N]'))[0].upper().strip()
    if continuar == 'N':
        break
print(50*'-=')
print(f'Ao todos, você cadastrou {len(galera)}')
print(f'O maior peso foi {max(peso_lista)}Kg. Peso de ', end='')
for p in galera:
    if max(peso_lista) in p:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi {min(peso_lista)}Kg. Peso de ', end='')
for p in galera:
    if min(peso_lista) in p:
        print(f'[{p[0]}]', end=' ')
print(50*'-=')