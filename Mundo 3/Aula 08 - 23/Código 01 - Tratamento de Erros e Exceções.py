"""
 Tratamento de Erros e Exceções
 Exemplo :
   print(x) - EXECEÇÃO! - NameError
   A varíavel X não foi declarada
try:
    operação
exept:
    falhou
else: # Opicional
    deu certo
finally: # Opicional
     # Ocorre mesmo sé apresentar falha
    certo/falha
   """

try:  #Obrigatório
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:  #Obrigatório
    print('Infelizmente tivemos um probelma')
else:  # Opcional
    print(f'O resultado é {r:.2f}')
finally:  # Opicional
    # Ocorre mesmo sé apresentar falha
    print('Volte sempre! Muito obrigado')
