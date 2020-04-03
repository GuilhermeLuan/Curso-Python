#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

list = []
while True:
    list.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] '))[0].upper().strip()
    if continuar == 'N':
        break
list.sort(reverse=True)
print(40*'-')
print(f'Você digitou {len(list)} elementos')
print(f'Os valores em ordem decrescente são {list}')
if 5 in list:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')