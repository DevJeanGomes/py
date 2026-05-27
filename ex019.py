from random import choice
contador = 1
n = []

while contador < 5:
    nomes = input('Digite o nome do {}º aluno: '.format(contador))
    contador += 1
    n.append(nomes)

print('O nome escolhido foi: {}\n'.format(choice(n)))