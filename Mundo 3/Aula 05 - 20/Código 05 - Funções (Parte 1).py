#Desempacotamento
def contador(*num): #*num ele vai pegar todos os parâmetros e jogar dentro de num, pois não sei a quantidade de parâmentros que irei receber
    for valor in num:
        print(valor, end=' ')
    print('FIM!')
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
contador(8, 0)


def contador1(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador1(5, 7, 3, 1, 4)
contador1(8, 4, 7)
contador1(8, 0)
