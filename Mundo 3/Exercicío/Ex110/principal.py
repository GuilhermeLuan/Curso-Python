# Exercício Python 110
# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda_4 as moeda

price = float(input('Digite um preço: R$'))
moeda.resumo(price, 20, 12)
# print(f'A metade de {moeda.formatacao(price)} é {moeda.metade(price, True)}')
# print(f'O dobro de {moeda.formatacao(price)} é {moeda.dobro(price, True)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(price, 10, True)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(price, 13, True)}')
