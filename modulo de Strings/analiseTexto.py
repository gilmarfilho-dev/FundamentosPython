nome = input("Digite seu nome: ")

print("Olá, ", nome, "! Seja bem vindo(a) ao nosso programa de análise de texto. \n")  # Exibe uma mensagem de boas-vindas ao usuário
print("O seu nome em letras maiúsculas é: ", nome.upper())  # Exibe o nome em letras maiúsculas
print("O seu nome em letras minúsculas é: ", nome.lower())  # Exibe o nome em letras minúsculas
print("O seu nome sem espaços tem ", len(nome.replace(" ", "")), "Caracteres")  # Exibe a quantidade de caracteres do nome sem espaços

nome = nome.split()  # Divide o nome em uma lista de palavras
print("A primeira palavra do seu nome tem ", len(nome[0]), "caracteres.")



