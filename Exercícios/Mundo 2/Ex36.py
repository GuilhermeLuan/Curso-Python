casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
p = casa / (anos*12) #prestacão
sal = salario * 30/100

if p > sal:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de {:.2f} \nEmpréstimo NEGADO !'.format(casa,anos,p))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de {:.2f} \nEmpréstimo ACEITO !'.format(casa,anos,p))