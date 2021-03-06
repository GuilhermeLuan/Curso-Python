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
        gols.append((int(input(f'   Quantos gols na partida {p+1} ? '))))

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] '))[0].upper().strip()
        if continuar not in 'SN':
            print('ERRO! Digite apenas S/N')

    dados['Gols'] = gols
    dados['Total'] = sum(gols)

    time.append(dados.copy())

    if continuar == 'N':
        break
    
print(25*'-=')

print(f"{'cod':<4} {'Nome':<15} {'Gols':^15} {'Total':>10}")
print(50*'-')
for k, v in enumerate(time):
    print(f"{k:<4} {v['Nome']:<15}  {str(v['Gols']):^15} {v['Total']:^13}")

print(50*'-')
while True:
    show = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if show == 999:
        break
    try:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[show]["Nome"]}')
        for k, v in enumerate(time[show]['Gols']):
            print(f'    No jogo {k + 1} fez {v} gols')
    except:
        print(f'ERRO! Não existe jogador com o número {show}')

print(f'{"<<< FIM DO PROGRAMA >>>":^50}')
