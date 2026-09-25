numero = int(input("Digite um número inteiro: "))
base = int(input('''Digite a base para conversão: 
                 1 - binário, 
                 2 - octal 
                 3 - hexadecimal: '''))

if base == 1:
    resultado = bin(numero)[2:]  # Remove o prefixo '0b'
    print(f"O número {numero} em binário é: {resultado}")
elif base == 2:
    resultado = oct(numero)[2:]  # Remove o prefixo '0o'
    print(f"O número {numero} em octal é: {resultado}")
elif base == 3:
    resultado = hex(numero)[2:].upper()  # Remove o prefixo '0x' e converte para maiúsculas
    print(f"O número {numero} em hexadecimal é: {resultado}")
else:
    print("Base de conversão inválida. Por favor, escolha entre 1, 2 ou 3.")