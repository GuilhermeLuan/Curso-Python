#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
expresao = str(input('Digite a expressão: '))

for item in expresao:
    if item in '(':
        lista.append(item)
    elif item in ')':
        if '(' in lista:
            lista.remove('(')
        else:
            lista.append(item)

if len(lista) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão não está valida')
