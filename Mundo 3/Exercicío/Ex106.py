#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep

cores = {"limpa":"\033[m", 
    "azul":"\033[7;36m",
    "roxo":"\033[7;35m",
    "negrito":"\033[1m",
    "branco":"\033[7m",
    "verde":"\033[7;32m",
    "amarelo":"\033[33m",
    "vermelho":"\033[7;31m"}


while True:
    print(f"{cores['verde']}="*25)
    print(f'{"Sistema de ajuda PyHelp":^25}')
    print(f'='*25)

    print(cores['limpa'], end='')
    opcao = str(input('Função ou Biblioteca (Fim para sair.) > '))

    if opcao .upper() == 'FIM':
        break
    print(f"{cores['azul']}~" * 50)
    print(f'{f"Acessando o manual do comando {opcao.upper()}":^50}')
    print(f'~'*50)
    print(cores['limpa'], end='')

    sleep(1)

    print(cores['branco'])
    help(opcao)

print(f"{cores['vermelho']}~"*10)
print(f'{"ATÉ LOGO":^10}')
print(f"{cores['vermelho']}~"*10)
