numeros = []

while len(numeros) < 5:
    numeros.append(float(input('Digite um número: ')))

soma = 0

for n in numeros:
    soma += n

print(f'A soma dos 5 números é {soma} e a média é {soma/5}')
