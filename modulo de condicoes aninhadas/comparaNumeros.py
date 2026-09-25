n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


if n1 > n2:
    print(f"O primeiro número ({n1}) é maior que o segundo número ({n2}).")
elif n1 < n2:
    print(f"O segundo número ({n2}) é maior que o primeiro número ({n1}).")
else:
    print(f"Os dois números são iguais: {n1} = {n2}.")