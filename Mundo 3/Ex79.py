#Exercício Python 079:
#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista_valores = []
while True:
    valor = int(input('Digite um valor: '))

    valor_nao_em_list = valor not in lista_valores     # Verifica se o valor não está na lista
    valor_em_list = valor in lista_valores     # Verifica se o valor está na lista

    lista_valores.append(valor)

    if valor_nao_em_list:
        print('Valor adicionado com sucesso...')
    if valor_em_list:
        print('Valor duplicado! Não vou adicionar... ')
        lista_valores.pop()

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print(20*'-=')
print(f'Você digitou os valores {sorted(lista_valores})')
"""
#OUTRA SOLUÇÃO

lista2 = []

while True:
    valor2 = int(input('Digite um valor: '))
    if valor2 in lista2:
        print('Valor duplicado! Não vou adicionar:')
    if valor2 not in lista2:
        lista2.append(valor2)
        print('Valor adicionado com sucesso... ')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(30*'-')
print(f'Você digiou os valores {lista2.sort()}')