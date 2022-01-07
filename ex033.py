pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))
menor = pri
if seg < pri and seg < ter:
    menor = seg
if ter < pri and ter < seg:
    menor = ter
maior = pri
if ter > pri and ter > seg:
    maior = ter
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
