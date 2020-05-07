# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.


def text(msg='', txt=True):
    if txt:
        print(30 * '-')
        print(f'{msg}'.center(30))
        print(30 * '-', flush=False)
    else:
        print(30 * '-')


def menu_principal():
    text('MENU PRINCIPAL')
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do sistema', flush=True)
    text(txt=False)


def start_interface():
    from time import sleep
    menu_principal()
    while True:
        try:
            escolha = int(input('Sua opção: '))
            if escolha == 3:
                text('Saindo do sistema... Até logo!')
                quit()
        except (TypeError, ValueError):
            print('ERRO: por favor, digite um número inteiro válido.', flush=False)
            sleep(0.3)
        else:
            if escolha > 3:
                print('ERRO: por favor, digite opção válida.', flush=False)
                sleep(0.3)
                menu_principal()
            if escolha == 1:
                text('OPÇÃO 1')
                sleep(0.3)
            if escolha == 2:
                text('OPÇÃO 2')
                sleep(0.3)
