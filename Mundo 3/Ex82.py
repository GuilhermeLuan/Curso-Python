#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso,crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
lista_pares = []
lista_impas = []
lista_num = []
while True:
    num = int(input('Digite um número: '))
    lista_num.append(num)

    if num % 2 == 0:
        lista_pares.append(num)
    elif num % 2 == 1:
        lista_impas.append(num)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] '))[0].upper().strip()
    if continuar == 'N':
        break
print(50*'-=')
print(f'A lista completa é {lista_num}\nA lista de pares é {lista_pares}\nA lista de ímpares é {lista_impas}')