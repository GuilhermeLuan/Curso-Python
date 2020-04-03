num = int(input('Digite um numero: '))

e = int(input('Escolha uma das bases para conversão \n [1] conveter para BINÁRIO \n [2] conveter para OCTAL \n [3] conveter para HEXADECIMAL \n Sua Opcão: '))

if e == 1:
    print('{} convertido para BINÁRIO é igual a "{}"'.format(num,bin(num).strip('0b')))
elif e == 2:
    print('{} convertido para OCTAL é igual a "{}"'.format(num,oct(num).strip('0o').upper()))
elif e == 3:
    print('{} convertido para HEXADECIMAL é igual a "{}" '.format(num,hex(num).strip('0x').upper()))
elif e > 3:
    print('\033[31m -=-=-=-= Opcão invalida -=-=-=-=  \033[31m')