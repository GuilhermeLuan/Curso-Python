# Móludos e Pacotes
# Modolarização - Ato de construir modulos
#   Objetivo: Dividir um programa grande, aumantar a legibilidade, facilitar a manutenção
import uteis

num = int(input('Digite um valor '))
fat = fatorial(num)
print(f'O factorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')
