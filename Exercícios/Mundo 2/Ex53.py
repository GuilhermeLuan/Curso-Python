frase = str(input('Digite uma frase: ')).strip().upper().replace(" ", "")
frase1 = frase[::-1]
print('O inverso de {} é {}'.format(frase,frase1))
if frase == frase1:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase não é um pelídromo')
