numero = 0
while True:
    numero = int(input('Digite um número entre 1 e 10: '))
    if numero >=1 and numero <=10:
        break
    else:
        print('O número deve ser algum entre 1 e 10.')

print(f'Tabuada de {numero}:')
for multiplicador in range(1, 11):
    print(f'{numero} X {multiplicador} = {numero * multiplicador}')
