#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
lista = []
expressão = str(input('Digite uma expressão: '))

for item in expressão:
    if '(' in item:
        lista.append('(')
    if ')' in item:
        if '(' in lista:
            lista.remove('(')
        else:
            lista.append(')')
print(lista)
if len(lista) == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão não está correta')
