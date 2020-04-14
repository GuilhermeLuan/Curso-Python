'''
Exempo 01:

    print('-------------')
    print('    Sistema de Alunos    ')
    print('-------------')

    print('-------------')
    print('    Cadastro de funcionários    ')
    print('-------------')

    print('-------------')
    print('    Erro de sistema      ')
    print('-------------')

Podemos otimizar esse código da seguinte forma:
    def mostraLinha():
        print('-------------')


Agora o Código fica assim:
    mostraLinha()
    print('Sistema de Alunos')
    mostraLinha()

    mostraLinha()
    print('Cadastro de funcionários')
    mostraLinha()

    mostraLinha()
    print('Erro de sistema')
    mostraLinha()

Temos uma forma melhor de otimizar esse código

def mensagem(msg): # nesse caso 'msg' será sistema de alunos
    print('-------------')
    print(msg) # Msg ira receber a mensagem(Sistema de alunos)
    print('-------------')

mensagem('Sistema de alunos) # esse texto será diretamento copiado para o parâmetro
'''

def lin(): # Quando iniciamos o programa a função não é executada, só vai executar o programa quando for chamado 
    print(30*'-')

#Programa Principal
lin() # Chama a função com o nome "lin"
print('     CURSO EM VÍDEO      ')
lin()
print('     Python      ')
lin()
print('     Aprenda Python      ')
lin()
