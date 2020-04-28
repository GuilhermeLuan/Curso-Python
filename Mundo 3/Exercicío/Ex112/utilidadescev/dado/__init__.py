def leiaDinheiro(valor=0):
    while True:
        valor = str(input(valor)).strip() #Valor_t = valor tranformado
        if valor.isnumeric():
            if ',' in valor:
                a = f'{valor}'.replace(',', '.')
                valor = float(a)
                return valor
            else:
                valor = float(valor)
                return valor
        else:
            print(f'ERRO: "{valor}" é um preço inválido.')

