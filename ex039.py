from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Qual o seu sexo? [M] / [F]: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')
if sexo == 'm' or 'M':
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print(f'Ainda falta(m) {saldo} ano(s) para o alistamento')
        ano = atual + saldo
        print(f'Seu alistamento será no ano de {ano}')
    elif idade > 18:
        saldo = idade - 18
        print(f'Você deveria ter se alistado há {saldo} anos')
        ano = atual - saldo
        print(f'Você se alistou em {ano}')
else:
    print('Mulheres não tem o alistamento obrigatório!')




