'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
media = 0
lista = []
while True:
    continuar = ' '
    dados = {'Nome': ' ',
    'Sexo': ' '}
    dados['Nome'] = str(input('Nome: '))

    while dados['Sexo'] not in 'MF':
        dados['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if dados['Sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))

    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N] ')).upper().strip()[0]
        lista.append(dados)
        if continuar not in 'SN':
            print('ERRO! Por favor, digite apenas S ou N.')

    if continuar == 'N':
        break

for i in lista:
    media = media + i['idade']

print(30*"-=")
print(f'A) Ao todos temos {len(lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media / len(lista):.2f}')
print(f'C) As mulheres cadastradas foram ',end='')
for e in lista:
    if e['Sexo'] == 'F':
        print(f'{e["Nome"]}', end=' ')
print()

print(f'D) Listas das pessoas que estão acima da média: ')

for e in lista:
    for k, v in e.items():
        if e['idade'] > media / len(lista):
            print(f'{k} = {v}: ',end='')
    print()
print('FIM')
