from random import shuffle

nomes = []
contador = 1

while contador < 5:
    nomes_alunos = input('Digite o nome do {}º aluno: '.format(contador))
    contador += 1
    nomes.append(nomes_alunos)

shuffle(nomes)

print('A ordem sorteada é: {}'.format(nomes))