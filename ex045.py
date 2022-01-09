import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(1, 3) #pc escolhe um número aleatório entre 1 e 3
print('''Escolha uma das opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print(f'Computador jogou {itens[pc]}')
if pc == 1:#pc jogou pedra
   if jogador == 1:
        print('EMPATE')
   elif jogador == 2:
        print('JOGADOR VENCE')
   elif jogador == 3:
        print('COMPUTADOR VENCE')
   else:
        print('JOGADA INVÁLIDA!')
elif pc == 2: #pc jogou papel
    if jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 3: #pc jogou tesoura
    if jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    elif jogador == 3:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA!')

