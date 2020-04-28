def leiaDinheiro(valor):
    while True:
        n = str(input(valor)).strip()
        if ',' in n or '.' in n or n.isnumeric():
            n = f'{n}'.replace(',', '.')
            valor = float(n)
            return valor
        else:
            print(f'ERRO:{n} é um preço inválido! ')
