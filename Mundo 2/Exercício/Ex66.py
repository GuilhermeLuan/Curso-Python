#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
count = n = 0
while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    count += 1
    n = num + n
print(f"A soma dos {count} valores foi {n}!")