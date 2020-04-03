#Exercício Python 078:
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []

for v in range(0,5):
    valores.append(int(input(f'Digite um valor para a posicão {v}: ')))
print(20*'-=')

print(f'Você digitou os valores: ', end='')

for v in valores:
    print(f'{v}', end=' ')

maior = max(valores)
menor = min(valores)

print(f'\nO maior valor digitado foi {max(valores)} nas posições', end=' ')
for p, val in enumerate(valores):
    if val == maior:
        print(f'{p}... ', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições', end=' ')
for p, val in enumerate(valores):
    if val == menor:
        print(f'{p}... ', end='')
