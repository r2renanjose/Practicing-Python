preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
desc = preço - novo
print('O produto que custava R$ {:.2f}, com 5% de desconto, vai custar R$ {:.2f}'.format(preço, novo))
print('Valor do desconto: R$ {:.2f}'.format(desc))
