qtd_temperaturas = 0
temperaturas = []
qtd_temperaturas = int(input('Quantidades de temperaturas: '))

for _ in range(0, qtd_temperaturas):
    temperatura = float(input('Digite temperatura: '))
    temperaturas.append(temperatura)

minima = maxima = temperaturas[0]
for temp in temperaturas:
    if minima > temp:
        minima = temp
    if maxima < temp:
        maxima = temp

print(f'''
A média das temperaturas é {sum(temperaturas)/qtd_temperaturas:.1f} º
A mínima é {minima:.1f} º
A máxima é {maxima:.1f} º
''')

