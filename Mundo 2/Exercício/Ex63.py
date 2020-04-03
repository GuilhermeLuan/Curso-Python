
print(20*"-")
print("Sequência de Fibonacci")
print(20*"-")

cont = 2
t1 = 0
t2 = 1
termos = int(input("Quantos termos você quer mostrar? "))

print('0 -> 1 ->',end=' ')
while cont != termos:
    resultado = t1 + t2
    t1 = t2
    t2 = resultado
    cont += 1
    print(f"{resultado}",end=' -> ')
print('FIM')
