cont = num = 0
list = []
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    cont += 1
    list.append(num)
    if num == 999:
        cont -= 1
        list.remove(999)
print(f'Você digitou {cont} e a soma entre eles foi {sum(list)}') 
    