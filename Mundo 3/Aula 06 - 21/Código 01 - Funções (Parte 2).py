
# DOCSTRINGS - É uma string para a documentação de uma função

# def contador(i, f, p):
#     # As docstrings começam aqui:
#     '''
        # -> Faz uma contagem e mostra na tela.
        # :param i: início da contagem
        # :param f: fim da contagem
        # :param p: passo da contagem
        # :return: sem retorno
#     '''
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!')

# contador(2, 10, 2)

# help(contador)

def contador(i, f, p):
    #As docstrings começam aqui:
    """ 
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')

contador(2, 10, 2)

help(contador)
