v = float(input('Qual sua velocidade atual ? '))
multa = (v-80) * 7
if v > 80:
    print('MULTADO ! Você excedeu o limite permitido que é de 80Km/h \
       \n Você deve pagar um multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com seguranca !')

