MaiorPeso = float(0.0)
MenorPeso = float(0.0)

for contador in range (1, 6):
    peso = float(input(f'\nDigite o peso da {contador}º pessoa: '))

    if contador == 1:
        MaiorPeso = peso
        MenorPeso = peso

    elif peso < MenorPeso:
        MenorPeso = peso

    elif peso > MaiorPeso:
        MaiorPeso = peso

print(f'\nO maior peso é: {MaiorPeso}KG,e o menor é: {MenorPeso}KG\n')