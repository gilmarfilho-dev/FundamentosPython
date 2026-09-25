from datetime import datetime
ano_atual = datetime.now().year

anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual - anoNascimento

if idade < 18:
    print("Você ainda não pode se alistar.")
    print(f"Você tem {idade} anos, e ainda faltam {18 - idade} anos para o alistamento.")
elif idade == 18:
    print("Você deve se alistar imediatamente.")
else:
    print("Você já passou da idade de alistamento.")
    print(f"Você tem {idade} anos, e deveria ter se alistado há {idade - 18} anos.")
    