# Exercício Python 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que seja

from utilidadescev import moeda
from utilidadescev import dado

price = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(price, 20, 12)
