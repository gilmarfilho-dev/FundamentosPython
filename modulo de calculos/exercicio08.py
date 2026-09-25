kms = int(input("Digite a distância em quilômetros que o carro ja percorreu: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco = (dias * 60) + (kms * 0.15)

print('O valor total a ser pago pelo aluguel do carro é de R$ {:.2f}'.format(preco))