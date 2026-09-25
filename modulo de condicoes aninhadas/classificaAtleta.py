from datetime import datetime
ano_atual = datetime.now().year
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"O atleta tem {idade} anos e está na categoria MIRIM.")
elif 9 < idade <= 14:
    print(f"O atleta tem {idade} anos e está na categoria INFANTIL.")
elif 14 < idade <= 19:
    print(f"O atleta tem {idade} anos e está na categoria JÚNIOR.")
elif 19 < idade <= 20:
    print(f"O atleta tem {idade} anos e está na categoria SÊNIOR.")
else:
    print(f"O atleta tem {idade} anos e está na categoria MASTER.")