votos = {'A': 0, 'B': 0, 'C': 0, 'nulos': 0}
qtd_eleitores = 0
qtd_eleitores = int(input('Quantos eleitores há? '))

for _ in range(0, qtd_eleitores):
    voto = input('Vote! Candidato A, B ou C? ')
    if voto.upper() == 'A':
        votos['A'] += 1
    elif voto.upper() == 'B':
        votos['B'] += 1
    elif voto.upper() == 'C':
        votos['C'] += 1
    else:
        votos['nulos'] += 1

print('\n')
for c, v in votos.items():
    if c != 'nulos':
        print(f'O caditado {c} recebeu {v} voto(s)')
    else:
        print(f'Voto(s) nulo(s): {v}')
