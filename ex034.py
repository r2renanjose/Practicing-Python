sal = float(input('Qual o salário atual do colaborador? R$ '))
if sal <= 2000:
    ns = sal * 15 / 100
    print(f'Quem ganhava R$ {sal}, passará a ganhar R$ {sal + ns:.2f}')
if sal > 2000:
    ns = sal * 10 / 100
    print(f'Quem ganhava R$ {sal}, passará a ganhar R$ {sal + ns:.2f}')