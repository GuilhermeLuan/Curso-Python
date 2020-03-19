#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$:'))
fin = int(input('Quantos anos de financiamente? '))

#Tranforma os anos em messes
f = fin * 12
#Calcula a prestacão
prestacao = vcasa / fin
#30% do salario
salario_f = salario * 30/100

print(f"Para pagar uma casa de R${vcasa} em {fin} anos a prestação será de {prestacao:.2f}")

if prestacao < salario_f:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("O Empréstimo não pode ser CONCEDIDO!")