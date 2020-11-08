numero = int(input('Digite o número que deseja o fatorial: '))

fatorial = 1
aux = numero
numeros = []
numeros.append(str(aux))

while aux > 1:
    fatorial *= aux
    aux -= 1
    numeros.append(str(aux))

print(f'O fatorial de: {numero}')
print(f'{numero}! = ', end='')
print(f'{" . ".join(numeros)} = {fatorial}')