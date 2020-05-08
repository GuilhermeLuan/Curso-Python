# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
from time import sleep

def text(msg='', txt=True):
    if txt:
        print(30 * '-')
        print(f'{msg}'.center(30))
        print(30 * '-', flush=False)
    else:
        print(30 * '-')


def menu_principal():
    text('MENU PRINCIPAL')
    print('\033[34m1 - Ver pessoas cadastradas\033[m')
    print('\033[34m2 - Cadastrar nova Pessoa\033[m')
    print('\033[34m3 - Sair do sistema\033[m', flush=True)
    text(txt=False)


def start_interface():
    menu_principal()
    validation()


def validation():
    while True:
        try:
            escolha = int(input('\033[32mSua opção: \033[m'))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m', flush=False)
            sleep(0.3)
        else:
            if escolha == 1:
                text('OPÇÃO 1')
                sleep(0.3)
            elif escolha == 2:
                text('OPÇÃO 2')
                sleep(0.3)
            elif escolha == 3:
                text('Saindo do sistema... Até logo!')
                quit()
            elif escolha <= 0 or escolha > 3:
                print('\033[31mERRO: por favor, digite opção válida.\033[m', flush=False)
                sleep(0.3)
                menu_principal()
