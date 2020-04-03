s = str(input("Infrome seu sexo: [M/F] ")).upper()
while s not in 'MmFf':
        s = str(input('Dados inválidos. Por favor, infrome seu sexo:'))
print(f'Sexo {s.upper()} registrado com sucesso')
