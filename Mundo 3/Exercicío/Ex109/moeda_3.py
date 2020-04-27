# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.



def dobro(v=0, form=False):
    res = v * 2
    if form:
        return formatacao(res)
    return res


def metade(v=0, form=False):
    res = v / 2
    if form:
        return formatacao(res)
    return res


def aumentar(v=0, taxa=0, form=False):
    res = v + (v * taxa/100)
    if form:
        return formatacao(res)
    return res


def diminuir(v=0, taxa=0, form=False):
    res = v - (v * taxa/100)
    if form:
        return formatacao(res)
    return res


def formatacao(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')
