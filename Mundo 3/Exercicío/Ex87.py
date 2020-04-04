'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

lista = [[], []]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            lista[0].append(matriz[linha][coluna])
            
print(30*'=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]',end='')
    print()
print(30*'=')

print(f'A soma dos valores pares é {sum(lista[0])}')
for c in range(0, 3):
    lista[1].append(matriz[c][2])

print(f' A soma dos valores da terceira coluna é {sum(lista[1])}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
