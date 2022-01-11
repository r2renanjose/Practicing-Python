real = float(input('Quanto dinheiro você tem na carteira?  R$ '))
dolar = real / 5.74
euro = real / 6.47
print('com R$ {:.2f} você pode comprar U$$ {:.2f} ou então £ {:.2f}'.format(real, dolar, euro))


