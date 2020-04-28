# Exercício Python 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111,
# temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função imputa(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários

def leiaDinheiro(valor):
    while True:
        n = str(input(valor)).strip()
        if ',' in n or '.' in n or n.isnumeric():
            n = f'{n}'.replace(',', '.')
            valor = float(n)
            return valor
        else:
            print(f'ERRO:{n} é um preço inválido! ')
