numeros = []

while len(numeros) < 10:
    numeros.append(float(input('Digite um número: ')))

pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'A quantidade de números pares é é {pares} e de ímpares é {impares}')
