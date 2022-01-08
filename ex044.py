print('==========LOJAS ORIGINAIS==========')
preço = float(input('Valor total da compra: R$ '))
avistad = preço - (preço * 15 / 100)
avistac = preço
cartao2x = preço + (preço * 5 / 100)
cartao3x = preço + (preço * 15 / 100)
parcela2x = cartao2x / 2
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 4x ou mais no cartão')
pagamento = int(input('Qual a sua opção? '))
if pagamento == 1:
    print(f'Sua compra de \033[1mR$ {preço:.2f}\033[m terá 15% de desconto e custará \033[1mR$ {avistad:.2f}\033[m.')
elif pagamento == 2:
    print(f'Valor da compra: \033[1mR$ {preço:.2f}\033[m pagamento no cartão (débito ou 1x direto no crédito).')
elif pagamento == 3:
    print(f'Sua compra de \033[1mR$ {preço:.2f}\033[m terá 5% de juros e custará \033[1mR$ {cartao2x:.2f}\033[m.\nValor da parcela: \033[1mR$ {parcela2x:.2f}\033[m.')
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas?'))
    divisao = cartao3x / parcelas
    totalparcelado = divisao * parcelas
    print(f'Sua compra de \033[1mR$ {preço:.2f}\033[m será parcelada em {parcelas}x de \033[1mR$ {divisao:.2f}\033[m\nValor total parcelado \033[1mR$ {totalparcelado:.2f}')


