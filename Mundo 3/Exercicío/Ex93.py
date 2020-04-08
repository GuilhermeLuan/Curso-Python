'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total 
'''
dados = {}
gols = []

dados['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for p in range(0, partidas):
    gols.append((int(input(f'Quantos gols na partida {p} ? '))))

dados['Gols'] = gols
dados['Total'] = sum(gols)

print(30*'-=')
print(dados)
print(30*'-=')

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(30*'-=')

print(f"O jogador {dados['Nome']} jogou {partidas} partidas.")
for i, e in enumerate(gols):
    print(f'    => Na partida {i}, fez {e} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
