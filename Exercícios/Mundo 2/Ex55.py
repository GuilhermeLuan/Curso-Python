#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for c in range(1,6):
    peso = float(input(f"Peso da {c} pessoa: "))
    lista.append(peso)

print(f"O maior pesso lido foi {max(lista)}Kg")
print(f"O maior pesso lido foi {min(lista)}Kg")
