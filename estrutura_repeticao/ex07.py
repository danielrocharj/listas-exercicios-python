numeros = []

while len(numeros) < 5:
    numeros.append(float(input('Digite um número: ')))

maior = numeros[0]

for n in numeros:
    if maior < n:
        maior = n

print(f'O maior número digitado é {maior}')
