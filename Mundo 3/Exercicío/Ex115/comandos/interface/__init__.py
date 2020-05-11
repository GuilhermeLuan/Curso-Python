# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.


def leia(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERROEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def text(msg='', txt=True):
    if txt:
        print(30 * '-')
        print(f'{msg}'.center(30))
        print(30 * '-', flush=False)
    else:
        print(30 * '-')


def menu(lista):
    text('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f"\033[32m{c} - \033[m\033[34m{i}\033[m")
        c += 1
    text(txt=False)
    opcão = leia('\033[32mSua opção: \033[m')
    return opcão


