largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
litros_tinta = area / 2

print('A área da parede é de {:.2f} m2'.format(area))
print('Para pintar a parede, você irá precisar de {:.2f} litros de tinta'.format(litros_tinta))
