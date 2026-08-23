MaiorDeIdade = 0
MenorDeIdade = 0
idade = 0


for contador in range (1, 8):
    AnoDeNascimento = int(input(f'\nDigite o ano de nascimento da {contador}º pessoa: \n'))

    idade = (2026 - AnoDeNascimento)

    if idade >= 21:
        MaiorDeIdade += 1
    else:
        MenorDeIdade += 1

print(f'\n{MaiorDeIdade} pessoas sao maiores de idade, e {MenorDeIdade} sao menores de idade.\n')