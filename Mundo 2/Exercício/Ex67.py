#           Exercício Python 067
#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
cout = 0
print(50*"-")
num = int(input("Quer ver a tabuada de qual valor ?"))
print(50*"-")
while True:
    cout += 1
    valor = num * cout
    print(f"{num:.2f} X {cout:.2f} = {valor:.2f}")
    if cout == 10:
        print(50*"-")
        num = int(input("Quer ver a tabuada de qual valor ?"))
        print(50*"-")
        cout = 0
    if num < 0:
        break
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")