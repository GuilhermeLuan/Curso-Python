import random
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')

n1 = int(input('Em que número eu pensei ? ')) # Jogador tenta adivinhar
n2 = random.randint(0,5) # Numeros randons entre 0 e 5
print('Processando...')
sleep(2)
if n2 == n1:
    print('Você acertou ! ')
else:
    print('Ganhei, eu pensei no numero {} e não no {}'.format(n2,n1))

