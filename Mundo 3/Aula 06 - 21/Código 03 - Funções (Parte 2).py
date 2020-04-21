'''
Escopo de variáveis

Escopo Local:
    Uma variável global é declarada (criada) fora das funções e pode ser acessada por todas as funções presentes no módulo onde é definida.
    Variáveis globais também podem ser acessadas por outros módulos, caso eles importem o módulo onde a variável foi definida.
    Uma aplicação útil de variáveis globais é o armazenamento de valores constantes no programa, acessíveis a todas as funções.
    Sempre devemos tomar cuidado ao alterar o valor de uma global dentro de uma função. Se for atribuído valor a ela, será na verdade criada uma nova variável, local, com o mesmo nome da global.
Escopo Global:
    Uma variável global é declarada (criada) fora das funções e pode ser acessada por todas as funções presentes no módulo onde é definida.

'''
# N funciona no código todo, ela é um escopo global

def teste():
    x = 8 #Escopo local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')



#Programa Principal
x = 2 # Escopo global
n = 2 #Escopo global
print(f'No programa principal, n vale {n}')
teste()
print(f'No programa principal, x vale {x}') #ERRO! Pois ele foi delcado somente na funcão, e recebe o nome de escobo local