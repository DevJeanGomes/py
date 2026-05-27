from random import randint
nus = int(input('\nDe o seu palpite para o valor: '))
npc = randint(0,5)

if nus == npc:
    print(f'\nParabens, voce acertou o numero sorteado foi: {npc}\n')
else:
    print(f'\nQue azar, o numero sorteado foi {npc}\n')