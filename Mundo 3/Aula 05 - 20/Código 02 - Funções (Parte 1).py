'''
Exemplo 2:

    print('----------------------------------')
    print('    Sistema de Alunos    ')
    print('----------------------------------')

    print('----------------------------------')
    print('    Cadastro de funcionários    ')
    print(----------------------------------')

    print('----------------------------------)
    print('    Erro de sistema      ')
    print(----------------------------------')

Podemos otimizar esse código da seguinte forma:

def mensagem(msg): # 'msg' é o parâmetro
    print('-------------')
    print(msg) # Msg ira receber a mensagem(Sistema de alunos)
    print('-------------')

mensagem('Sistema de alunos) # esse texto será diretamento copiado para o parâmetro

'''


def título(msg):  # msg é o parâmetro
    print(30*'-')
    print(msg)
    print(30*'-')


#Programa Principal
título('     CURSO EM VÍDEO      ')
título('     Python      ')
título('     Aprenda Python      ')
