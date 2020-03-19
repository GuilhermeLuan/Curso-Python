#Exercício Python 075:
#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num_par = []
num = (int(input('Digite um número:')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('Você digitou os valores', end=' ')

for n in num:
    if n % 2 == 0:
        num_par.append(n)
    print(n, end=' ')

print(f'\nO valor 9 apareceu {num.count(9)} vezes.')

try:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição.')
except ValueError:
    print('O valor 3 não foi digitado.')

print(f'Os valores pares digitados foram.', end=' ')
for par in num_par:
    print(par, end=' ')
