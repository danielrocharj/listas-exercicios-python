numero = int(input('Digite um número inteiro: '))
contador = 0
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        contador += 1

if contador > 2:
    print('O número não é primo')
else:
    print('O número é primo')
