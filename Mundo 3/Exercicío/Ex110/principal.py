# Exercício Python 110
# Adicione o módulo moeda.py criado nos desafios anteriores,
# uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
import moeda_4 as moeda

price = float(input('Digite um preço: R$'))
moeda.resumo(price, 20, 12)
