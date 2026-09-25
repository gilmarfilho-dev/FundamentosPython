carteira = float(input('Informe o saldo atual na sua carteira: '))
dolar = 3.27

conversao = carteira / dolar

print('Voce tem {} reais, com isso é possível comprar {:0.2f} dólar(es)'.format(carteira, conversao))
