print(30*'-')
print('Sequência de Fibonacci')
print(30*'-')
termo = int(input('Quantos termos você quer mostras? '))
print(30*'~')
t1 = 0
t2 = 1
resultado = t1 + t2
print(t1,end=' ')
while termo > 1:
    print(resultado,end=' ')
    resultado = t1 + t2
    t1 = t2
    t2 = resultado
    termo = termo - 1

