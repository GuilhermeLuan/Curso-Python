print('Gerador de PA \n')
print(10*'-')

termo = int(input("Primeiro termo: "))
pa = int(input("Razão do PA: "))
cont = 1
cont2 = 1
opcao = 1
mais_termos = 1
print(termo,end= ' -> ')

while cont < 10:
    s1 = termo + pa
    cont += 1
    termo = s1
    cont2 += 1
    print(s1, end=' -> ')
print('PAUSA')
while True:
    cont = 0
    mais_termos = int(input("Quantos termos você deseja mostrar a mais? "))
    if mais_termos == 0:
        print(f'Prograssãp finalizada com {cont2} termos mostrados.')
        break
    while cont < mais_termos:
        s1 = termo + pa
        cont += 1
        cont2 += 1
        termo = s1
        print(s1, end=' -> ')
    print('PAUSA')
