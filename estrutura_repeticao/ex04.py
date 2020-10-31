pop_a = 80000
tx_cres_a = 3
pop_b = 200000
tx_cres_b = 1.5

anos = 0
while pop_a < pop_b:
    pop_a *= (1 + tx_cres_a/100)
    pop_b *= (1 + tx_cres_b/100)
    anos += 1

print(f'Levará {anos} anos para que a população de A ultrapasse ou iguale a população de B')
