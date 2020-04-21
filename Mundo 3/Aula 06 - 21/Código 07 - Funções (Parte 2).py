def fatorial(num=1):
    f = 1 # Variável local
    for c in range(num, 0, -1):
        f *= c
    return f

n = int(input('Digite um número: '))#Variável Global
print(f'O factorial de {n} é igual a {fatorial(n)}')
