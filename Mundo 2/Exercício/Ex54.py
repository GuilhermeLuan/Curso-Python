#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. 
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year
menor = maior = 0
for c in range(1, 8):
    nasc = int(input(f"Em que ano a {c} pessoas nasceu? "))
    mn = ano - nasc
    if mn >= 21:
       maior = maior + 1
    else:
        menor = menor + 1
print(f"Ao todo tivemos {maior} pessoas meiores de idade \nE também tivemos {menor} pessoas menores de idade")
