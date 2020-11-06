numero = int(input('Digite um número inteiro: '))
contador = 0
limite_divisor = round(numero/2) + 1

for divisor in range(1, limite_divisor):
    if numero > 2 and numero % 2 == 0:
        contador = 99  # não importa o valor aqui, desde que seja maior que 2
        break
    if numero % divisor == 0:
        contador += 1

if contador > 2:
    print('O número não é primo')
else:
    print('O número é primo')
