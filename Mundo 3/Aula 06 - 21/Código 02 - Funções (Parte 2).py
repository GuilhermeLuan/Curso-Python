'''
Parâmetros opcionais -  Às vezes não temos a necessidade de passar um parâmetro a uma função, usando um valor padrão previamente codificado para o parâmetro em questão
'''
def somar(a=0, b=0, c=0):
    #Os três parâmetros são opicionais. O valor padrão é 0. 
    #Se fornecer um argumento, eles irão receber o valor do argumento.
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    '''
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(c=4, a=2)
somar(8, 4) # Vai retornar um erro caso eu não use os parâmetros opcionais
somar() # Vai retornar um erro caso eu não use os parâmetros opcionais
