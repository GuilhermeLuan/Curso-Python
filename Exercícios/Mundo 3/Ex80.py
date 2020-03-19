#Exercício Python 080:
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.

valores = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('O valor foi inserido no final lugar')
    else:
        for i in range(0, 5):
            if n <= valores[i]:
                valores.insert(i, n)
                print(f'O número foi adicionado na posição {i}')
                break
print(f'Os valores digitados em ordem foram {valores}')