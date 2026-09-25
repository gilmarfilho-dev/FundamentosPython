import random

numero_secreto = random.randint(0, 5)

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 0 e 5.")

usuario = int(input("Digite o seu palpite: "))

if usuario == numero_secreto:
    print("Parabéns! Você acertou o número secreto!")
else:
    print(f"Que pena! O número secreto era {numero_secreto}. Tente novamente!")