#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print(20*"=")
print("      Banco yGui      ")
print(20*"=")
c50 = c20 = c10 = c1 = 0

while True:
    valor = int(input('Qual valor você quer sacar ?'))
    c50 = valor // 50
    valor = valor - (c50*50)
    c20 = valor // 20
    valor = valor - (c20*20)
    c10 = valor // 10
    valor = valor - (c10*10)
    c1 = valor // 1
    valor = valor - (c1*1)

    if c50 > 0:
        print(f"Total de {c50} cédulas de R$50")
    if c20 > 0:
        print(f"Total de {c20} cédulas de R$20")
    if c10 > 0:
        print(f"Total de {c10} cédulas de R$10") 
    if c1 > 0:
        print(f"Total de {c1} cédulas de R$1")
    print(20*"=")
    print('Volte sempre ao banco yGui! Tenha um bom dia!')
    break

