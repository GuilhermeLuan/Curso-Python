nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')

print('Seu nome em maiúsculas é {}'.format(nome.upper()))

print('Seu nome minúsculas é {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

div = nome.split()[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(div,len(div)))