numero = int(input('Digite um número inteiro: '))
divisores = []
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores.append(divisor)

if len(divisores) > 2:
    print(f'O número não é primo e o divisores são: {divisores}')
else:
    print('O número é primo')