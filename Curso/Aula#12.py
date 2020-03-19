nome = str(input('Qual é o seu nome? '))
#Condicão simples, apenas if
if nome == 'Guilherme':
    print('Que nome bonito !')
elif nome =='Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia ':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}'.format(nome))