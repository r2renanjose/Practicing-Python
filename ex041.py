from datetime import date
atual = date.today().year
nas = int(input('Qual o ano do nascimento do atleta? '))
idade = atual - nas
if idade <= 9:
    print(f'O atleta tem {idade} e é da categoria MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} e é da categoria INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} e é da categoria JUNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} e é da categoria SÊNIOR')
else:
    print(f'O atleta tem {idade} e é da categoria MASTER')