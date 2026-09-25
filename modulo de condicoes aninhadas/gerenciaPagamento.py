produto = float(input("Informe o valor do produto: "))
print("O valor do seu produto é R${}".format(produto))
formasPagamento = input('''Escolha uma das formas de pagamento: 
                        [1] para Dinheiro/Cheque
                        [2] para Cartão à vista
                        [3] para Cartão parcelado em 2x
                        [4] para Cartão parcelado em 3x ou mais
                        Qual é a opção? 
                        ''')
if formasPagamento == 1:
    print("Sua forma de pagamento é Dinheiro/Cheque, 10% de desconto.")
    valorFinal = produto * 0.1
    print("O valor final do seu produto com desconto ficou: R${} reais".format(valorFinal))
elif formasPagamento == 2:
    print("Sua forma de pagamento é cartão à vista, 5% de desconto.")
    valorFinal = produto * 0.05
    print("O valor final do seu produto com desconto ficou: R$ {} reais".format(valorFinal))
elif formasPagamento == 3:
    valorFinal = produto / 2
    print("Sua compra será parcelada em 2x de {}".format(valorFinal))
elif formasPagamento == 4:
    valorFinal = produto + (produto * 0.2)
    totParcelas = int(input("Quantas parcelas?"))
    parcelas = valorFinal / totParcelas
    print("Seu produto será parcelado em {}x e teve {:.2f} reais de juros." .format(totParcelas, parcelas))
    print("O valor do final do produto foi ", valorFinal)
else:
    valorFinal = produto
    print("Opção de pagamento inválida")
print("Sua compra de {}, vai custar {} no final" .format(produto, produto))
    