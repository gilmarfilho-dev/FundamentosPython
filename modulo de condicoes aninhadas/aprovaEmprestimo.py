valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu salário: "))
tempoFinanciamento = int(input("Digite em quantos anos deseja financiar: "))

prestacao = valorCasa / (tempoFinanciamento * 12)

print(f"Valor da prestação mensal: {prestacao:.2f}")

if prestacao > (salario * 0.3):
    print("Empréstimo não aprovado. A prestação excede 30% do seu salário.")
else:
    print("Empréstimo aprovado. A prestação está dentro do limite permitido.")
