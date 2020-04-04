'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
lista = []
temp = []
while True:
    continuar = ' '
    nome = str(input('Nome: '))
    temp.append(nome)
    for c in range(1, 3):
        nota = float(input(f'Nota {c}: '))
        temp.append(nota)
        
    lista.append(temp[:])
    temp.clear()

    continuar = str(input('Quer continuar ? [S/N]'))[0].upper().strip()
    if continuar == 'N':
        break

print(25*'-')
print(f'{"No.":^3} {"NOME":^10} {"MÉDIA":^5}')

print(20*'-')
for i, l in enumerate(lista):
    print(f'{i:^3} {lista[i][0]:^10} {sum(lista[i][1:])/2:^5.1f} ')
print(50*'-')

while True:
    show_nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if show_nota == 999:
        break
    try:
        print(f'Notas de {lista[show_nota][0]} são {lista[show_nota][1:]}')
    except IndexError:
        print('Esse aluno não esta registado no banco de dados !!!')
    print(50*'-')
