from datetime import datetime
ano_atual = ano = datetime.today().year
ano = int(input('Ano de Nascimento: '))
idade = ano_atual - ano

print('O atleta tem {}'.format(idade))

if idade <= 9:
    print('Classificação: MIRIN')
elif idade <= 14:
    print('Classificação: INFATIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')
