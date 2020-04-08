p = float(input('Qual é o preço do produto ? R$'))
n = p - (p * 5 / 100)

print('O produto que custava R${:.2f}, na promocao vai custar {:.2f}'.format(p, n))