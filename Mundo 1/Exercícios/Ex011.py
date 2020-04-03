L = float(input("Largura da parede: "))
A = float(input("Altura da parede: "))
area = L * A
t = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(L, A ,area ))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(t))
