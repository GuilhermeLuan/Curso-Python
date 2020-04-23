'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''
def voto(msg):
    from datetime import date
    ano = date.today().year
    idade = ano - msg

    print(f'Com {idade} anos:',end=' ')

    if idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

#Programa principal
pergunta = int(input('Em que ano você nasceu? '))
print(voto(pergunta))
