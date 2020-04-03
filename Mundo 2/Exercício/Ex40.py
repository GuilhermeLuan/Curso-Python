nota1 = float(input('Primeira nota: '))
#{:.1f}
nota2 = float(input('Segunda nota: '))
cal = (nota1 + nota2) / 2

if cal >= 7.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f} '.format(nota1,nota2,cal))
    print('O Aluno esta APROVADO')
elif cal <= 6.9 or cal >= 5:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2,cal))
    print('O Aluno está de RECUPERAÇÃO')
elif cal <= 5.0:
    print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1,nota2.call))
    print('O aluno está REPROVADO')