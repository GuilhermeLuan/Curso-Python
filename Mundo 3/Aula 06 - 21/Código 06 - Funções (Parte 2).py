'''
Retorno de valores 
'''
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s #Ele retorna o valor para a função

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
