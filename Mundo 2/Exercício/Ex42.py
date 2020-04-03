r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

triangulo = r1 < r2 + r3 and r1 < r1 + r3 and r3 < r1 + r2
equi = r1 == r2 == r3
iso = r1 == r2 and r3 != r1 and r3 != r2 or r3 == r2 and r3 != r1 or r1 == r3 and r1 != r2
escaleno = r1 != r2 != r3

if triangulo and equi:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
elif triangulo and iso:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
elif triangulo and escaleno:
    print('Os segmentos acime PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos não podem f4ormar um triângulo')