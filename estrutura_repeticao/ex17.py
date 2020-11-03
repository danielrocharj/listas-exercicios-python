numero = int(input('Digite o número que deseja o fatorial: '))

fatorial = 1
aux = numero
while aux > 1:
    fatorial *= aux
    aux -= 1

print(f'O fatorial de {numero} é {fatorial}')
