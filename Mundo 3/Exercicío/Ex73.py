                    #Exercício Python 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

def listras():
        print(30*'-=')

time = ( 'Flamengo', 'Palmeiras', 'Santos',
        'São Paulo', 'Internacional', 'Corinthians',
        'Grêmio', 'Athletico-PR','Bahia','Goiás','Vasco da Gama', 'Atlético', 'Botafogo',
        'Fortaleza', 'Ceará SC', 'Fluminense', 'Cruzeiro','CSA', 'Chapecoense', 'Avaí')
listras()
print(f'A lista de times do Brasileirão: {time}')
listras()
print(f'Os 5 primeiros times são: {time[0:5]}')
listras()
print(f'Os 4 últimos são: {time[16:]}')
listras()
print(f'Os times em ordem alfabética: {sorted(time)}')
listras()
print(f'O Chapecoense está na {time.index("Chapecoense") + 1} posição')
listras()
