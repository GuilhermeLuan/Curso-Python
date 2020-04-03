soma = 0
count = 0
for c in range(1,7):
    n = int(input('{}ª Número:'.format(c)))
    if n % 2 == 0:
        soma = soma + n
        count = count + 1
print('Você informou {} números PARES e a soma foi {}'.format(count,soma))