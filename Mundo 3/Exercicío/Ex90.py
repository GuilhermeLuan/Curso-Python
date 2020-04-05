'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
Abaixo de 7 - recuperação
Abaixo de 5 - reprovacão
7 ou mais - aprovado
'''
dados = {}

dados['nome'] = str(input('Nome: ')).strip()
dados['média'] = float(input(f'Média de {dados["nome"]}: '))


if dados["média"] >= 7: # 7 ou mais
    dados['situacão'] = 'Aprovado'

elif 5 <= dados["média"] < 7: # Abaixo de 7
   dados['situacão'] = 'Recuperação'

elif dados['média'] < 5:   #Abaixo de 5 
    dados['situacão'] = 'Reprovado'

print(f'  - nome do aluno é {dados["nome"]}')
print(f'  - A média de {dados["nome"]} é {dados["média"]}')
print(f'  - A situação é igual a {dados["situacão"]}')
