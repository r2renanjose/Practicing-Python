print('-'*95)
salário = float(input('                            Qual o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
aumento = novo - salário
print('  o funcionário que ganhava R$ {:.2f}, passará a ganhar R$ {:.2f}, com os 15% de reajuste'.format(salário, novo))
print('                                >>>Valor do aumento: R$ {:.2f}<<<'.format(aumento))
print('-----O NOVO SALÁRIO TERÁ VIGOR A PARTIR DO PRIMEIRO DIA ÚTIL DO MÊS SUBSEQUENTE AO AUMENTO-----')
print('-'*95)
print('                                                                powered by Rsys - V: 01258/2021')
