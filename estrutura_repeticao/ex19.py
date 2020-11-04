from random import randint

quantidade = -1

while quantidade < 0 or quantidade > 1000:
    quantidade = int(input('Entre com a quantidade de números para o conjunto: '))
    if quantidade < 0 or quantidade > 10:
        print('Valor deve ser entre 0 e 1000')

conjunto = []

for _ in range(quantidade):
    conjunto.append(randint(0, quantidade))

print(conjunto)

soma = 0
maior = menor = conjunto[0]
for numero in conjunto:
    if maior < numero:
        maior = numero
    if menor > numero:
        menor = numero
    soma += numero

print(f'O menor valor é {menor}, o maior valor é {maior} e o somatório é {soma}')
