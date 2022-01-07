import time
vel = float(input('Qual a velocidade do veículo? '))
if vel > 80:
    print('"MULTADO!" Limite de 80 km/h excedido!')
    m = (vel - 80) * 7
    print('PROCESSANDO VALOR DA MULTA...')
    time.sleep(2)
    print(f'Valor da multa aplicado: R$ {m}')
print(f'-={vel}=-')

