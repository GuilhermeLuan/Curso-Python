# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda_2 as moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.formatacao(price)} é {moeda.formatacao(moeda.metade(price))}')
print(f'O dobro de {moeda.formatacao(price)} é {moeda.formatacao(moeda.dobro(price))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumentar(price, 10))}')
