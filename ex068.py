from random import randint

usuario = int(input('\nDe o seu palpite para o valor: '))
pc = randint(0,10)


while usuario != pc:
    print(f'\nQue azar, o numero sorteado foi {pc}\n')
    usuario = int(input('\nDe outro palpite para o valor: '))
    pc = randint(0,10)

print(f'\nParabens, voce acertou o numero sorteado foi: {pc}\n')

