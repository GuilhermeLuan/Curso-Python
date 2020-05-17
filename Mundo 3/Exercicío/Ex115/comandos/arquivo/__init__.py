def arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        print(f'Arquivo {nome} criado com sucesso!')
        arquivo = open(nome, 'wt+')
        arquivo.close()


def LerArquivo(nome):
    arq = open("cursoemvideo.txt", "r")
    conteu = arq.readlines()
    pessoas = []
    for cont in conteu:
        pessoas.append(cont.replace("\n", ""))
    for v, i in enumerate(pessoas):
        if v % 2 == 0:
            print(f"{i:<30}", end="")
        else:
            print(f"\t{i:<3} anos")


def CadastrarPessoa(nome='<desconhecido>', age=0):
    try:
        arq = open("cursoemvideo.txt", 'r')
    except Exception as error:
        print(f'ERRO! {error.__class__}')
    else:
        try:
            conteudo = arq.readlines()
            conteudo.append(nome + '\n')
            conteudo.append(str(age) + '\n')
            arq = open("cursoemvideo.txt", "w")
            arq.writelines(conteudo)
            arq.close()
        except Exception as error:
            return print(f'ERRO AO TENTAR GRAVAR INFROMAÇÃO. {error.__class__}')
        else:
            print(f'Registro {nome} cadastrado com sucesso')
