def resumo(v=0, aumenta=10, diminui=5):
    """
        -> Realiza formatação do valor passado para dinheiro
        :param v: Valor digitado
        :param aumenta: Aumenta em um percentagem X
        :param diminui: Diminui em um percentagem Y
    """
    print(30*'-')
    print(f"{'RESUMO DO VALOR':^30}")
    print(30 * '-')
    print(f'Preço analisado: \t{formatacao(v)}')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço \t{metade(v, True)}')
    print(f'{aumenta}% de aumento: \t{aumentar(v, aumenta, True)}')
    print(f'{diminui}% de redução: \t{diminuir(v, diminui, True)}')
    print(30 * '-')
