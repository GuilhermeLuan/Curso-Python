"""
Móludos e Pacotes
Modolarização - Ato de construir modulos
    Objetivo: Dividir um programa grande, aumantar a legibilidade, facilitar a manutenção"""
from uteis import numeros

num = int(input('Digite um valor '))
fat = numeros.fatorial(num)
print(f'O factorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
