'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
A) A soma de todos os valores pares digitados. X
B) A soma dos valores da terceira coluna. X
C) O maior valor da segunda linha. X
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            matriz[3].append(matriz[linha][coluna])
            
print(30*'=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]',end='')
    print()
print(30*'=')

print(f'A soma dos valores pares é {sum(matriz[3])}')
for c in range(0, 3):
    matriz[4].append(matriz[c][2])
print(f'A soma dos valores da terceira coluna é {sum(matriz[4])}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
