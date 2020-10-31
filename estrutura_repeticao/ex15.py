termo = int(input('Digite a qunatidade de termos: '))

atual = 1
anterior = 0
passo  = 1

while passo <= termo:
    print(atual, end = ' ')
    anterior, atual = atual, atual + anterior
    passo += 1
