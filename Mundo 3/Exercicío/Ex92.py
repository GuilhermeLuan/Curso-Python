'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além
'''
from datetime import date

dados = {}

dados['Nome'] = str(input("Nome: "))
dados['Ano'] = int(input("Ano de Nascimento: "))
dados['Idade'] = date.today().year - dados['Ano']
dados['Ctps'] = int(input("Carteina de Trabalho (0 não tem): "))

if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratacão: '))
    dados['Salário'] = float(input('Salário: R$: '))
    dados['aponsetadoria'] = (dados['Contratação'] - dados['Ano']) + 35

del dados['Ano']
print(50*'-=')
for k, v in dados.items():
    print(f"{k} tem o valor {v}")
