a = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" apareceu {} vezes na frase'.format(a.count('A')))
print('A primeria letra "A" apareceu na posicão {} '.format(a.find('A')+1))
print('A ultima letra "A" aparaceu na posicão {} '.format(a.rfind('A')+1))