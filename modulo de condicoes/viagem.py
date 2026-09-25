distancia = int(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    print("O preço da sua passagem é: R$ 0,50 por km")
    print("Valor total da passagem: R$", distancia * 0.50)
else:
    print("O preço da sua passagem é: R$ 0,45 por km")
    print("Valor total da passagem: R$", distancia * 0.45)