'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

números = []
def sorteia():
    for n in range(0, 5):
        números.append(randint(0,10))
    print('Sorteado 5 valores da lista: ',end='')
    for n in números:
        print(f'{n}',end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')



sorteia()
print(números)
