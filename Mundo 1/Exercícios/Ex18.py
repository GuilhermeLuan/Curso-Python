import math
an = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(an))
print('o Angulo de {} tem o SENO de {:.2f}'.format(an, seno))
co = math.cos(math.radians(an))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(an, ta))