def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somandos os valores {valores} temos {s}')
    

    
soma(5, 2)
soma(2, 9, 4)