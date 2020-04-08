palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO')

for c in palavras:
    print(f'\nNa palavra {c} temos',end=' -> ')
    if c.count('A') >= 1:
        print(c.count('A')*'a ', end='')
    if c.count('E') >= 1:
        print(c.count('E')*'e ',end='')
    if c.count('I') >= 1:
        print(c.count('I')*'i ',end='')
    if c.count('O') >= 1:
        print(c.count('O')*'o ',end='')
    if c.count('U') >= 1:
        print(c.count('U')*'u ')

print(30*'-')
print(f'{" Outra Soluçao":^30}')
print(30*'-')
for p in palavras:
    print(f'\nNa palavra {p} temos',end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra}',end=' ')
