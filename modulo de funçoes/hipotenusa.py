from math import hypot

cat_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
cat_oposto = float(input("Digite o comprimento do cateto oposto: "))

print('O comprimento da hipotenusa é {:.2f}' .format(hypot(cat_adjacente, cat_oposto)))