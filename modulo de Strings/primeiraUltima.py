frase = input("Digite uma frase: ")
print("A letra A aparece", frase.count("A"), "vezes na frase.")
print("A primeira letra A aparece na posição", frase.find("A") + 1)
print("A última letra A aparece na posição", frase.rfind("A") + 1)