numero = -1
executa = True
def condicao(n):
    return numero % 1 != 0 or (numero < 0 or numero > 16)
while executa:
    while condicao(numero):
        numero = float(input('Digite o número que deseja o fatorial: '))
        if condicao(numero):
            print('Os números devem ser inteiros, positivos e menores que 16')
        else:
            numero = int(numero)

    fatorial = 1
    aux = numero
    while aux > 1:
        fatorial *= aux
        aux -= 1

    print(f'O fatorial de {numero} é {fatorial}')
    desejo = input('Deseja interomper a execução (S/N)?')
    numero = -1
    executa = False if desejo.lower() == 's' else True
