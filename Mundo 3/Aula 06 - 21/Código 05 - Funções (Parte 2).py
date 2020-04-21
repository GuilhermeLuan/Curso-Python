def teste(b):
    global a # Estou dizando para o python não criar uma variável "a", use o "a" global.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 #Escopo Global
teste(a)
print(f'A fora vale {a}')
