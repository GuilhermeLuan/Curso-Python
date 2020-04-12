def dobre(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobre(valores)
print(valores)
