#Faça um programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Qual tamanho em metros quadrados ?'))
tinta = area / 3 # informa a quatidade de litros
count = 0 # Contador 

while True:
    if tinta >= 18:
        tinta -= 18
        count += 1
    if tinta < 0:
        break
print(count)