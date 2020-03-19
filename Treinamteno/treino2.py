#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#1- salário bruto.
#2- quanto pagou ao INSS.
#3- quanto pagou ao sindicato.
#4- o salário líquido.

salario_horas = float(input('Quanto você ganha por hora ? '))
horas = float(input('Quantas horas você trabalhar por mês ?'))

#Salário bruto
salario = salario_horas * horas

#imposto de renda 11%
ir = (salario * 11 / 100)

#INSS
inss = (salario * 8 / 100)

#sindicato
s = (salario * 5/ 100)

#Salário líquido
sl = salario - ir - inss - s

print('+ Salário Bruto : R${:.2f}'.format(salario))
print('- IR (11%) : R${:.2f}'.format(ir))
print('- INSS (8%) : R${:.2f}'.format(inss))
print('- Sindicato ( 5%) : R${:.2f}'.format(s))
print('= Salário líquido: R${:.2f}'.format(sl))