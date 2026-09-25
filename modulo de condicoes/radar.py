velocidade = int(input("Digite a velocidade do veículo em km/h: "))
multa = 0

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado por excesso de velocidade!")
    print("Valor da multa: R$ 7,00 por cada km acima do limite.", multa)
    print("Valor total da multa: R$", multa)

else:
    print("Parabéns! Você está dentro do limite de velocidade.")