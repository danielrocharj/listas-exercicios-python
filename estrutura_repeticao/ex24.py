qtd_notas = 0
notas = []
qtd_notas = int(input('Quantas notas você digitará?'))

for _ in range(0, qtd_notas):
    notas.append(float(input('Digite a nota: ')))

print(f'A média das notas é {sum(notas)/qtd_notas:.2f}')
