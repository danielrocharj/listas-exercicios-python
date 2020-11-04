from random import randint

n = int(input('Digite a quantidade de números para o conjunto: '))
conjunto = []

for _ in range(n):
    conjunto.append(randint(0, n*2))

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
