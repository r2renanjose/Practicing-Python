l = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
dim = l * a
tinta = a / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(l, a, dim))
print('Para pintar esta parede, você precisará de {}L de tinta.'.format(tinta))
