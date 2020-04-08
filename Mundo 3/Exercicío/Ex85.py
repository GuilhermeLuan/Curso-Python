"""
Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
lista = [[], []]
countp = counti = 0
for c in range(1, 8):
    num = int(input(f'Digite o {c}o. Valor: '))
    if num % 2 == 0:
        lista[0].append(num)
        countp += 1
    else:
        lista[1].append(num)
        counti += 1
print(40*'-=')
if countp >= 1:
    print(f'Os valores pares digitados foram: {sorted(lista[0])}')
if counti >= 1:
    print(f'Os valores Ímpares digitados foram: {sorted(lista[1])}')
