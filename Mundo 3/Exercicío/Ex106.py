#Exercício Python 106
#Faça um mini-sistema que utilize o Interactive Help do Python.
#O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
from time import sleep


def linha(msg='', cor='', apenas_cor=False):
    cores = {"limpa": "\033[m",
             "azul": "\033[7;36m",
             "roxo": "\033[7;35m",
             "negrito": "\033[1m",
             "branco": "\033[7m",
             "verde": "\033[7;32m",
             "amarelo": "\033[33m",
             "vermelho": "\033[7;31m"}

    if apenas_cor:
        print(cores[cor])
    else:
        tam = len(msg) + 2
        print(f"{cores[cor]}=" * tam)
        print(f'{msg.center(tam)}')
        print(f'=' * tam)
        print(cores['limpa'], end='')


while True:
    linha('Sistema de ajuda PyHelp', 'verde')
    opcao = str(input('Função ou Biblioteca (Fim para sair.) > '))
    if opcao .upper() == 'FIM':
        break
    linha('Acessando o manual do comando', 'azul')
    sleep(1)
    linha(cor='branco', apenas_cor=True)
    help(opcao)
linha('ATÉ LOGO', 'vermelho')
