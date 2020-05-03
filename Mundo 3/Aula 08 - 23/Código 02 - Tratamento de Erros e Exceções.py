"""
Tratamento de Erros e Exceções
 Um try pode ter varíos expects
"""

try:  # Obrigatório
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # Obrigatório
    # Declara o erro em uma varíavel.
    print(f'Problema encontrado foi {erro.__class__}')
else:  # Opcional
    print(f'O resultado é {r:.2f}')
finally:  # Opicional
    # Ocorre mesmo sé apresentar falha
    print('Volte sempre! Muito obrigado')
