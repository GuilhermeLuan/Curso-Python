s = float(input('Qual é o salario do funcionario? R$: '))
#Realiza a porcetagem
s1 = s+(s*10/100)
s2 = s+(s*15/100)
# If
if s >= 1250.00:
    print('Quem ganhava R${} vai ganhar R${:.2f}'.format(s,s1))
else:
    print('Quem ganhava R$ {} vai ganhar R${:.2f}'.format(s,s2))