# Exercício Python 108
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

price = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.formatacao(price)} é {moeda.formatacao(moeda.metade(price))}')
print(f'O dobro de {moeda.formatacao(price)} é {moeda.formatacao(moeda.dobro(price))}')
print(f'Aumentando 10%, temos {moeda.formatacao(moeda.aumentar(price, 10))}')
