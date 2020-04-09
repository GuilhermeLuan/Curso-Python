'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''
time = []
while True:
    dados = {}
    gols = []

    continuar = ' '
    dados['Nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append((int(input(f'   Quantos gols na partida {p} ? '))))

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] '))[0].upper().strip()
        
    dados['Gols'] = gols
    dados['Total'] = sum(gols)

    time.append(dados.copy())

    if continuar == 'N':
        break
    
print(30*'-=')
print(time)
print(30*'-=')

# for k, v in dados.items():
#     print(f'O campo {k} tem o valor {v}')
# print(30*'-=')

# print(f"O jogador {dados['Nome']} jogou {partidas} partidas.")
# for i, e in enumerate(gols):
#     print(f'    => Na partida {i}, fez {e} gols.')
# print(f'Foi um total de {dados["Total"]} gols.')
