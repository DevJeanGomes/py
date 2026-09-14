PrimeiroTermo = int(input('\nDigite o primeiro termo da sua PA: '))
razao = int(input('Digite a razao da sua PA: '))

termo = PrimeiroTermo
contador = 1
total_termos = 0
mais_termos = 10  # Começa pedindo 10 termos inicial de padrão

while mais_termos != 0:
    total_termos += mais_termos

    while contador <= total_termos:
        print(f'{termo} → ', end='')
        termo += razao
        contador += 1

    print('\nPAUSA')
    print('\nDigite 0 para finalizar')
    mais_termos = int(
        input('\nQuantos termos você quer mostrar a mais? ')
    )

print(f'\nProgressão finalizada com {total_termos} termos mostrados.\n')