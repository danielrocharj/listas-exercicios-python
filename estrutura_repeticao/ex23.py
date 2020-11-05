n = int(input('Digite um número inteiro: '))
contador_divisoes_geral = 0
primos = []
for numero in range(1, n + 1):
    if numero > 2 and numero % 2 == 0:
        continue
    divisor = contador = 1

    while divisor <= numero/2:
        if numero % divisor == 0:
            contador += 1
        divisor += 1

    if contador <= 2:
        primos.append(numero)
        contador_divisoes_geral += contador

print(f'{contador_divisoes_geral} divisões foram executadas para encontrar os números primos: {primos}')
