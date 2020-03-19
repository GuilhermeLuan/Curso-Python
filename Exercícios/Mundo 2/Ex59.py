import time
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    opcao = int(input("[ 1 ] Soma \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos números \n[ 5 ] Sair do programa\n>>>> Qual é sua opcão ? "))
    if opcao == 1:
        print(f'A soma entre {n1} + {n2} = {n1+n2}')
        print(20*"-")
        time.sleep(0.4)
    elif opcao == 2:
        print(f"O resultado de {n1} x {n2} é {n1*n2} ")
        print(20*"-")
        time.sleep(0.4)
    elif opcao == 3:
        print(f"Entre {n1} e {n2} o maior valor é {max(n1,n2)}")
        print(20*"-")
        time.sleep(0.4)
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif opcao > 5:
        print('Opção invalida. Tente novamente')
        time.sleep(0.4)
    elif opcao == 5:
        print('Finalizando...')
        time.sleep(0.4)
        print(20*'-')
