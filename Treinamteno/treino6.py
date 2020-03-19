#Exercício Python 037: 
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))
opcao = int(input("Escola uma das bases para conversão: \n[1] BINÁRIO\n[2] OCTALL\n[3] HEXADECIMAL \n Sua opção: "))

if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(num,bin(num).replace('0b','')))
if opcao == 2:
    print("{} convertido para OCTALL é igual a {}".format(num,oct(num).replace('0o','')))
if opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num).replace('0x','')))
    