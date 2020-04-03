d = float(input('Quantos dias alugados? '))
k = float(input('Quantos Km rodados? '))

d1 = d * 60
k1 = k * 0.15

print('O total a pagar é de R${:.2f}'.format(d1 + k1))
