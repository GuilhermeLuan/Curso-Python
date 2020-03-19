# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
time = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Internacional', 'Corinthians',
        'Grêmio', 'Athletico-PR','Bahia','Goiás','Vasco da Gama', 'Atlético', 'Botafogo',
        'Fortaleza', 'Ceará SC', 'Fluminense', 'Cruzeiro','CSA', 'Chapecoense', 'Avaí')
print(30*'-')
print('Consulta dos times')
print(30*'-')
while True:
    opcao = int(input('O que você dejesa consultar ?\n[1] Os 5 primeiros times.\n[2] Os últimos 4 colocados.\n[3] Times em ordem alfabética.\n[4] Em que posição está o time da Chapecoense.\nOpcão:'))
    if opcao == 1:
        print('Os 5 primeiros times são: {}'.format(time[0:5]))
    if opcao == 2:
        print('Os 4 últimos são: {}'.format(time[16:]))
    if opcao == 3:
        print('Os times em ordem alfabética: {}'.format(sorted(time)))
    if opcao == 4:
        print('O Chapecoense está na {}'.format(time.index('Chapecoense')))
    continuar = ' '
    if continuar not in 'SN':
        continuar = str(input('Deseja continuar ?[S/N] '))[0].upper()
        if continuar in 'NN':
            quit()

