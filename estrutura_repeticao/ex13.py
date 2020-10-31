num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

i = 1
resultado = 1

while i <= num2:
    resultado *= num1
    i += 1

print(f'{num1} elevado a {num2} é {resultado}')
