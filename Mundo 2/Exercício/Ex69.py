#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 
count18 = homen = mulheres = 0
while True:
    sexo = continuar = ' '
    print("Cadastre uma pessoa")
    idade = int(input("Idade: "))
    while sexo not in 'FM':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        count18 += 1
    if sexo in 'M':
        homen += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    while continuar not in 'SN':
        continuar = str(input("Quer continuar [S/N]")).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {count18}')
print(f'Ao todo temos {homen} homen(s) cadastrados')
print(f"E temos {mulheres} mulher(es) com menos de 20 anos")
