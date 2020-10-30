
while True:
    pop_a = int(input('Entre com a população do país A: '))
    if pop_a < 2:
        print('A população deve ser no mínimo 2 para que haja crescimento')
    else:
        break

while True:
    tx_cres_a = float(input('Entre com a taxa de crescrimento do país A: '))
    if tx_cres_a <= 0:
        print('Impossível crescer com taxa negativa ou igual a 0%')
    else:
        break

while True:
    pop_b = int(input('Entre com a população do país B: '))
    if pop_b < 2:
        print('A população deve ser no mínimo 2 para que haja crescimento')
    else:
        break

while True:
    tx_cres_b = float(input('Entre com a taxa de crescrimento do país B: '))
    if tx_cres_b <= 0:
        print('Impossível crescer com taxa negativa ou igual a 0%')
    else:
        break


anos = 0
while pop_a < pop_b:
    pop_a *= (1 + tx_cres_a/100)
    pop_b *= (1 + tx_cres_b/100)
    anos += 1

print(f'Levará {anos} anos para que a população de A ultrapasse ou iguale a população de B')
