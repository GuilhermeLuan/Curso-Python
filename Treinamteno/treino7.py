#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print('O PRIMEIRO valor é maior')
if n2 > n1:
    print('O SEGUNDO valor é maior')
if n1 == n2 or n2 == n1:
    print('Os valores são iguais ')