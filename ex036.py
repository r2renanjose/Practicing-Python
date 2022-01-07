casa = float(input('Qual o valor do imóvel: R$ '))
sal = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
min = sal * 30 / 100
print(f'Para pagar um imóvel no valor de R$ {casa:.2f} em {anos} anos, a prestação será de R$ {prest:.2f}')
if prest <= min:
    print('Financiamento APROVADO!')
else:
    print('Renda incompatível, financiamento REPROVADO!')
