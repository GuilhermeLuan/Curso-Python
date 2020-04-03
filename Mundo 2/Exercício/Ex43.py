peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura ? (m) '))
calculo = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f}'.format(calculo))

if calculo < 18.5:
    print('Você esta abaixo do peso normal !')
elif calculo >= 18.5 and calculo < 25 :
    print('Você esta no peso ideal !')
elif calculo >= 25 and calculo < 30:
    print('Você está sobrepeso !')
elif calculo >= 30 and calculo < 40:
    print('Você está em obesidade, cuidado!')
elif calculo >= 40:
    print('Você está em  obesidade mórbida, cuidado !')
