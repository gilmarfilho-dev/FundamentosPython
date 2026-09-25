salario = float(input("Digite o salário atual: "))

if salario > 1250:
    aumento = salario * 0.1
    print("O aumento será de 10% do salário atual.")
    print("Valor do aumento: R$", aumento)
else:
    aumento = salario * 0.15
    print("O aumento será de 15% do salário atual.")
    print("Valor do aumento: R$", aumento)
    
