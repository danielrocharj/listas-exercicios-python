sacola = []
while True:
    item = float(input('Preço do item: '))
    if item > 0:
        sacola.append(item)
    else:
        break

total = sum(sacola)
dinheiro = 0
while dinheiro < total:
    dinheiro = float(input('Dinheiro: '))
    if dinheiro < total:
        print('Quantidade de dinheiro insuficiente! Entre novamente!')

print(f'Lojas Tabajara')

for n, produto in enumerate(sacola):
    print(f'Produto {n}: R$ {produto:.2f}')

print(f'''
Total: {total:.2f}
Dinheiro: {dinheiro:.2f}
Troco: {(dinheiro - total):.2f}
''')


