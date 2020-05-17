"""
Tratamento de Erros e Exceções
 Um try pode ter varíos expects
"""

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print(f'Não é possível dividir um número por zero.')
except KeyboardInterrupt:
    print(f'O usuário preferiu não informar os dados! ')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre! Muito obrigado')
