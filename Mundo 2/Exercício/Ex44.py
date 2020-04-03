print('====== Lojas Guilherme ======')
preco = float(input('Preço das compras: R$'))
pagamento = int(input('FORMAS DE PAGMENTO \n'
                      '[1] à vista dinheiro/cheque\n'
                      '[2] à vista cartão\n'
                      '[3] 2x no cartão\n'
                      '[4] 3x ou mais no cartão\n'
                      'Qual é a opção? '))
if pagamento == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco - (preco * 10/100)))
elif pagamento == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco - (preco * 5/100)))
elif pagamento == 3:
    print('Sua compra será parcela em 2x de R${:.2f} sem juros'.format(preco/2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco))
elif pagamento == 4:
    parcela = int(input(print('Quantas parcelas ?')))
    if pagamento == 4:
        print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(parcela,(preco + (preco * 20/100))/parcela))
        print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco,preco + (preco * 20/100)))
elif pagamento > 4:
    print('OPCÃO INVALIDA !')
