r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('        Os segmentos acima PODEM FORMAR um Triangulo!', end=)
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    if r1 != r2 != r3:
        print('ESCALENO')
else:
    print('        Os segmentos acima NÃO PODEM FORMAR um Triangulo!')