"""
Exercício Python 113:
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
import ex113_funções as função

n1 = função.leiaInt('Digite um número inteiro: ')
n2 = função.leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2} ')
