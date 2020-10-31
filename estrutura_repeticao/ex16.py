atual = 1
anterior = 0
print(anterior, end = ' ')
while anterior <= 500:
    print(atual, end = ' ')
    anterior, atual = atual, atual+anterior
