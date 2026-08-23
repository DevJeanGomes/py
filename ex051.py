PrimeiroTermo = int(input('Digite o primeiro termo da sua PA: '))
razao = int(input('Digite a razao da sua PA: '))
termo = PrimeiroTermo + (10 - 1) * razao

for contador in range (PrimeiroTermo, termo, razao):
    print(f'{contador}', end=' -> ')
print('\nfim\n')