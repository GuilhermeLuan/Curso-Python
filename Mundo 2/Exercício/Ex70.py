#               Exercício Python 070
#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não.
#No final, mostre:
#   A) qual é o total gasto na compra.
#   B) quantos produtos custam mais de R$1000.
#   C) qual é o nome do produto mais barato.

menor = menor_nome = total = produto_1000 = cont = 0
print(50*'-')
print('LOJA SUPER BARATÃO')
print(50*'-')

while True:
    continuar = ' '
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if cont == 1 or preco < menor:
        menor = preco
        menor_nome = produto 

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    
    if preco > 1000:
        produto_1000 += 1

    if continuar == 'N':
        break
print(50*'-')
print(f'O total da compra foi R${total:.2f} \nTemos {produto_1000:.2f} produtos custando mais de R$1000.00 \nO produto mais barato foi {menor_nome} que custa R${menor:.2f}')
