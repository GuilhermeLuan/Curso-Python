continuar = ' '
lista = []
soma = 0
cont = 0
while continuar not in 'Nn':
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    lista.append(numero)
    continuar = str(input("Quer continuar? [S/N] "))
print(f"Você digitou {cont} números e a média foi {soma / cont} \nO maior valor foi de {max(lista)} e o menor foi {min(lista)}")

