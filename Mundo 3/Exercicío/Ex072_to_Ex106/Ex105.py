'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def notas(*num, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: um ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias infromações sobre a situação da turma.
    '''
    notas = {'total': len(num), 'maior': max(num),
    'menor': min(num), 'média': sum(num) / len(num)}
    if sit:
        if notas['média'] >= 5:
            situacão = 'RAZOÁVEL'
        if notas['média'] >= 7:
            situacão = 'BOA'
        else:
            situacão = 'RUIM'
        notas['situação'] = situacão
    return notas

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
