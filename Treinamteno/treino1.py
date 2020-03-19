# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

peixes = int(input("Qual foi o peso(kg) dos peixes hoje ?"))
excesso = (peixes - 50)
valor = excesso * 4

if peixes > 50:
    print("Você excedeu o limete de 50Kg, o excesso foi de {}KG e o valor é de R${}".format(excesso,valor))
else:
    print('Você não excedeu o limite de 50Kg, portanto não precisa pagar multa')
