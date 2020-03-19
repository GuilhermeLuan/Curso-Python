#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 ano
medidade = 0
idadem = 0
maior_nome = ''
maior = 0
for c in range(1,5):
    print(f"---- {c} Pessoa ----")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    medidade = idade + medidade
    sexo = str(input('Sexo [M/F]: ').upper().strip())

    if sexo == 'F' and idade < 20:
        idadem = idadem + 1

    if c == 1 and sexo == 'M':
        maior = idade
        maior_nome = nome
    else:
        if idade > maior:
            maior = idade
            maior_nome = nome
        
print(30*'-')
print(f"A média de idade do grupo é de {medidade / 4 :.1f} anos")
print(f'O homem mais velho tem {maior} anos e se chama {maior_nome}')
print(f"Ao todo são {idadem} mulheres com menos de 20 anos")