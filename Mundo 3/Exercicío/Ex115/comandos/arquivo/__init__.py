def criar_arquivo():
    try:
        arquivo = open('cursoemvideo.txt', 'r')
        arquivo.close()
    except FileNotFoundError:
        print('Arquivo cursoemvideo.txt criado com sucesso!')
        arquivo = open('cursoemvideo.txt', 'w')
        arquivo.close()


def pessoas():
    arquivo = open('cursoemvideo.txt', 'r')
    for linha in arquivo:
        print(linha.strip())
    arquivo.close()
