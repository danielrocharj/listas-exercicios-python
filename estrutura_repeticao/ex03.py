
while True:
    nome = input('Digite um nome: ')
    if len(nome) < 3:
        print('O nome deve ter mais que 3 caracteres.')
    else:
        break

while True:
    idade = int(input('Digite a idade: '))
    if idade < 0 or idade > 150:
        print('A idade deve ser entre 0 e 150.')
    else:
        break

while True:
    salario = float(input('Digite o salário: '))
    if salario <= 0:
        print('O salário deve ser maior que zero.')
    else:
        break

while True:
    sexo = input('Digite o sexo: ')
    if sexo != 'f' and sexo != 'm':
        print('Sexo inválido.')
    else:
        break

#Estado Civil: 's', 'c', 'v', 'd';
while True:
    civil = input('Digite o estado civil: ')
    if civil not in 'scvd':
        print('Estado civil deve ser s, c, v ou d.')
    else:
        break
