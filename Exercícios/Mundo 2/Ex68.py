#Exercício Python 068:
#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
cont = 0
from random import randint
print(25*"=")
print("VAMOS JOGAR PAR OU ÍMPAR")
print(25*"=")

while True:
    par_impar = ' '
    valor = int(input("Digite um valor: "))

    while par_impar not in 'PI':
        par_impar = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
    
    computador = randint(0,10)
    soma = valor + computador
    impa = soma % 2 == 1
    par = soma % 2 == 0

    def resultado():
        print(25*"=")
        print(f"Você jogou {valor} e o computador {computador}. Total de {soma} DEU {p_i} ")
        print(25*"=")


    if impa == True:
        if par_impar == 'I':
            p_i = 'ÍMPAR'
            resultado()
            print('VENCEU! \n Vamos jogar novamente...')
            cont += 1
            
        else:
            p_i = 'IMPÁR'
            resultado()
            print(f"GAME OVER! Você venceu {cont} vezes")
            break
            
    if par == True:
        if par_impar == 'P':
            p_i = 'PAR'
            resultado()
            print('VENCEU! \n Vamos jogar novamente...')
            cont += 1
        else:
            p_i = 'PAR'
            resultado()
            print(f"GAME OVER! Você venceu {cont} vezes")
            break        