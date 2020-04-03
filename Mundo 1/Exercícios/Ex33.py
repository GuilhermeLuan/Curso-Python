n1 = str(input('Digite o 1 valor: '))
n2 = str(input('Digite o 2 valor: '))
n3 = str(input('Digite o 3 valor: '))

if n1 > n2 and n1 > n3:
    print('O maior numero é {}'.format(n1))

if n2 > n1 and n2 > n3:
    print('O maior numero é {}'.format(n2))

if n3 > n1 and n3 > n2:
    print('O maior numero é {}'.format(n3))

#-----------------------------------------------------#

if n1 < n2 and n1 < n3:
    print('O menor numero é {}'.format(n1))

if n2 < n1 and n2 < n3:
    print('O menor numero é {}'.format(n2))

if n3 < n2 and n3 < n2:
    print('O menor numero é {}'.format(n3))

