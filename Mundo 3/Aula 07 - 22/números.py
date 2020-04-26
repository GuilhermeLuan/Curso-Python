# Móludos e Pacotes
# Modolarização - Ato de construir modulos
#   Objetivo: Dividir um programa grande, aumantar a legibilidade, facilitar a manutenção
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


num = int(input('Digite um valor '))
fat = fatorial(num)
print(f'O factorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')
