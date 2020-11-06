qtd_turmas = 0
turmas = []
qtd_turmas = int(input('Quantas turmas há?'))

for _ in range(0, qtd_turmas):
    while True:
        alunos = int(input('Digite a qtd de alunos dessa turma: '))
        if alunos > 40:
            print('As turmas não podem ter mais de 40 alunos')
        else:
            break
    turmas.append(alunos)

print(f'A média de alunos nas turmas é {sum(turmas)/qtd_turmas:.2f}')
