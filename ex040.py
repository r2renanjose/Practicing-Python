nome = str(input('Qual o nome do aluno? '))
mat = str(input('Qual a matéria? '))
pri = float(input(f'Digite a nota do primeiro bimestre de {nome} em {mat}:'))
seg = float(input(f'Digite a nota do segundo bimestre de {nome} em `{mat}:'))
ter = float(input(f'Digite a nota do terceiro bimestre de {nome} em {mat}:'))
qua = float(input(f'Digite a a nota do quarto bimestre de {nome} em {mat}:'))
media = (pri + seg + ter + qua) / 4
print(f'A média anual de {nome} foi: {media:.2f}')
if media >= 7:
    print(f'Aluno(a) Aprovado(a) em {mat}!')
elif media <7 or media > 6:
    print(f'ALuno(a) em Recuperação em {mat}!')
else:
    print(f'Aluno(a) Reprovado(a) em {mat}')
