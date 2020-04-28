# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.



def dobro(v=0, formato=False):
    """
        -> Realiza o calculo do dobro de um valor específico
        :param v: Valor digitado
        :formato: Parametro para a formatação da moeda
        :return: Retorna o dobro do valor digitado
    """
    res = v * 2
    return res if formato is False else formatacao(res)


def metade(v=0, formato=False):
    """
        -> Realiza o calculo da metade de um valor específico
        :param v: Valor digitado
        :formato: Parametro para a formatação da moeda
        :return: Retorna o valor com sua metade calculada
    """
    res = v / 2
    return res if formato is False else formatacao(res)


def aumentar(v=0, taxa=0, formato=False):
    """
        -> Aumenta o falor em X porcentagem e retorna seu valor
        :param v: Valor digitado
        :param taxa: Porcetagem
        :param formato: Parametro para a formatacão da moeda
        :return: Retorna o valor com o aumento com X porcentagem.
    """
    res = v + (v * taxa/100)
    return res if formato is False else formatacao(res)


def diminuir(v=0, taxa=0, formato=False):
    """
        -> Realiza a reduzão de um valor em X porcentagem
        :param v: Valor digitado
        :param taxa: Porcetagem
        :param formato: Parametro para a formatacão da moeda
        :return: Retorna o valor com a diminuição com X porcentagem.

    """
    res = v - (v * taxa/100)
    return res if formato is False else formatacao(res)


def formatacao(v=0, moeda='R$'):
    """
        -> Realiza formatação do valor passado para dinheiro
        :param v: Valor digitado
        :param moeda: Formatacão da moeda
        :return: Retorna o parâmetro passado em formato de reais (R$)
    """
    return f'{moeda}{v:.2f}'.replace('.', ',')
