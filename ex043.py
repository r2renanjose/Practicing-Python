print('-=-' * 15)
print('              \033[1mCALCULADORA IMC\033[m')
print('-' * 45)
peso = int(input(' ● Qual é o seu peso (Kg)? '))
altura = float(input(' ● Qual é a sua altura (m)? '))
imc = peso / (altura ** 2)
print(f'O seu IMC é igual a: {imc:.1f}')
if imc < 18.5:
    print('>>\033[1;31mAbaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('>>\033[1;32mPeso ideal\033[m')
elif imc >= 25 and imc < 29:
    print('>>\033[1;31mSobrepeso\033[m')
elif imc >= 29 and imc < 34.9:
    print('>>\033[1;31mObesidade I\033[m')
elif imc >= 34.9 and imc < 39.9:
    print('>>\033[1;31mObesidade II\033[m')
elif imc > 39.9:
    print('\033[1;31mObesidade Mórbida\033[m')



