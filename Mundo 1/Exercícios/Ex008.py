n = float(input("Uma distancia em metros: "))


km = n / 1000
hm = n / 100
da = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000

print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(da))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))