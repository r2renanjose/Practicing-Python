dist = float(input('Qual a distância da viagem em KM? '))
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print(f'O preço da sua passagem será: R$ {preço:.2f}')