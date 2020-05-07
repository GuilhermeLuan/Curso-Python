# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.


def text(msg):
    print(30 * '-')
    print(f'{msg}'.center(30))
    print(30 * '-')


def menu():
    global opcão
    número = (1, 2, 3)
    from time import sleep
    while True:
        text('MENU PRINCIPAL')
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova Pessoa')
        print('3 - Sair do sistema', flush=True)
        try:
            opcão = int(input('Sua opção: '))
            if opcão == 3:
                text('Saindo do sistema... Até logo!')
                quit()
        except (TypeError, ValueError):
            print('ERRO: por favor, digite um número inteiro válido.', flush=False)
            sleep(0.3)
        else:
            if opcão > 3:
                print('ERRO: por favor, digite opção válida.')
                sleep(0.3)
            if opcão == 1:
                text('OPÇÃO 1')
                sleep(0.3)
            if opcão == 2:
                text('OPÇÃO 2')
                sleep(0.3)
            if opcão == 3:
                text('OPÇÃO 3')
                sleep(0.3)
