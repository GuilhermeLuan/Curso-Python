soma = 0
count = 0
n = int(input('Digite um número: '))
for c in range(1,n+1):
    if n % c == 0:
        count = count + 1
    print(c,end=" ")

if count == 2:
    print('\nO número {} foi dividido 2 vezes \n'
          'E por isso ele É PRIMO'.format(n))
else:
    print('\nO número {} foi dividido {} \n'
          'E por isso ele NÃO É PRIMO'.format(n,count))
