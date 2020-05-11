# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
from time import sleep

from comandos import arquivo as a
from comandos import interface as i

a.criar_arquivo()
while True:

    res = i.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if res == 1:
        i.text('PESSOAS CADASTRADAS')
        a.pessoas()
        sleep(0.5)
    elif res == 2:
        i.text('Opção 2')
        sleep(0.5)
    elif res == 3:
        sleep(0.5)
        i.text('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção valida\033[m')
        sleep(0.5)
