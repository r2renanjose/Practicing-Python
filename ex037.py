num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases de conversão\n[ 1 ] converter em BINÁRIO\n[ 2 ] converter em OCTAL\n[ 3 ] converter em HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção invalida, tente outra opção')