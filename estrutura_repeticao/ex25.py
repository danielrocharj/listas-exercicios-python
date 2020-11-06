qtd_pessoas = 0
idades = []
qtd_pessoas = int(input('Quantas pessoas há na turma?'))

for _ in range(0, qtd_pessoas):
    idades.append(float(input('Digite a idade: ')))

media_idade = sum(idades)/qtd_pessoas

if media_idade <= 25:
    print('Turma Jovem')
elif media_idade <= 60:
    print('Turma Adulta')
else:
    print('Turma Idosa')