from random import randint
import time
pc = randint(0, 5) #faz o pc pensar em um número
print('-=-' *20)
print(' Vou pensar em um número de 0 a 5, tente adivinhar qual é!')
print('-=-' *20)
jg = int(input('Qual número você acha que eu pensei ? ')) #jogador chuta um número
print('PROCESSANDO...')
time.sleep(2)
if jg == pc:
    print('PARABÉNS! Você acertou na mosca!')
else:
    print(f'GANHEI! Eu pensei no número {pc}, e não no {jg}!')
