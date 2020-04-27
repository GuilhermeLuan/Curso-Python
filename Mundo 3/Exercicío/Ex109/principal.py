# Exercício Python 109:
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda_3 as moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.formatacao(price)} é {moeda.metade(price, True)}')
print(f'O dobro de {moeda.formatacao(price)} é {moeda.dobro(price, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(price, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(price, 13, True)}')