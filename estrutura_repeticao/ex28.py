cds = []
qtd_cds = 0
qtd_cds = int(input('Quantos cds há na coleção?'))

for _ in range(0, qtd_cds):
    cds.append(float(input('Digite o valor de compra desse CD: ')))

total_cds = sum(cds)
print(f'''
O valor total investido na coleção é {total_cds}
O valor médio gasto em cada um é {total_cds/qtd_cds:.2f}
''')
