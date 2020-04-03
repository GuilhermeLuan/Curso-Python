from datetime import datetime
ano = datetime.today().year
g = int(input('Selecione uma das opcoes: '
              '\n[1] Homem'
              '\n[2] Mulher'
              '\n Opcão: '))

d = int(input('Ano de nascimento: '))

n1 = ano - d  #Calcula a idade
n2 = 18 - n1
n3 = n1 - 18

if n1 < 18 and g == 1:
    print('Quem nasceu em {} tem {} anos em {}.'.format(d, n1, ano))
    print('Ainda faltam {} anos para o alistamento'.format(n2))
    print('Seu alistemento será em {}'.format(n2 + ano))
elif n1 > 18 and g == 1:
    print('Quem nasceu em {} tem {} nos em {}.'.format(d, n1, ano))
    print('Você ja deveria ter se alistado há {} anos'.format(n3))
    print('Seu alistamento foi em {}'.format(ano - n3))
elif n1 == 18 and g == 1:
    print('Quem nasceu {} tem {} em {}.'.format(d, n1, ano))
    print('Você tem que se alistar IMEDIATAMENTE ! ')
if g == 2:
    print('Você é mulher, por tanto não tem a obrigação de se alista!')


