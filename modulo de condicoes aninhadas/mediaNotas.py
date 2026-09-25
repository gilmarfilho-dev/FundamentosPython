nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"A média é {media:.2f}. Aprovado!")
elif media >= 5 and media <= 6.9:
    print(f"A média é {media:.2f}. Recuperação!")
else:
    print(f"A média é {media:.2f}. Reprovado!")