termo = int(input("Primeiro termo: "))
pa = int(input("Razão do PA: "))
cont = 1
na = termo
print(termo,end= ' -> ')

while cont < 10:
    s1 = termo + pa
    cont += 1
    termo = s1
    print(s1, end=' -> ')
print('FIM')


