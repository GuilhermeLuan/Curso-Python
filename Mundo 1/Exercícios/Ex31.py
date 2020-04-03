d = float(input('Qual a distancia da sua viagem ? '))
s1 = d * 0.50
s2 = d * 0.45

print('Você está prestes a comecar um viagem de {} Km.'.format(d))

if d >= 200:
    print('E o preco de sua passagem será de R${:.2f}'.format(s2))
else:
    print('E o preco de sua passagem será de R${:.2f}'.format(s1))
