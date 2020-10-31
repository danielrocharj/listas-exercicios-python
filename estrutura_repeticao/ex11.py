num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = 0
for n in range(num1+1, num2):
    soma += n

print(f'A soma dos número entre {num1} e {num2} é {soma}')
