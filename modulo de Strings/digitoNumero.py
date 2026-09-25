num = int(input("Digite um número de 0 a 9999: "))  # Solicita ao usuário que digite um número inteiro entre 0 e 9999
num = list(str(num))  # Converte o número em uma lista de caracteres

print("A unidade é: ", num[3]) # Exibe a unidade do número
print("A dezena é: ", num[2]) # Exibe a dezena do número
print("A centena é: ", num[1]) # Exibe a centena do número
print("A milhar é: ", num[0]) # Exibe a milhar do número