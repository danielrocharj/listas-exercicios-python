# 25. Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia
# entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

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