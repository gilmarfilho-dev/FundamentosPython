lado1 = int(input("Digite o valor do primeiro lado do triângulo: "))
lado2 = int(input("Digite o valor do segundo lado do triângulo: ")) 
lado3 = int(input("Digite o valor do terceiro lado do triângulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os lados formam um triângulo.")
else:
    print("Os lados não formam um triângulo.")