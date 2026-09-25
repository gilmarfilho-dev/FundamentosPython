produto = float(input('Informe o preço do produto: '))
desconto = produto * 0.05

precofinal = produto - desconto

print('O preço final do produto com desconto é de R$ {:.2f}'.format(precofinal))
