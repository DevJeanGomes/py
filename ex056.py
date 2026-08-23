SomaIdade = 0
MaiorIdadeHomem = 0
NomeHomemMaisVelho = ''
MulheresMenos20 = 0

for contador in range(1, 5):
    nome = input(f'\nDigite o nome da {contador}ª pessoa: ').strip().upper()
    idade = int(input(f'Digite a idade da {contador}ª pessoa: '))
    sexo = input(f'Digite o sexo da {contador}ª pessoa (F/M): ').strip().upper()

    # 1. Soma a idade para calcular a média no final
    SomaIdade += idade

    # 2. Descobre o homem mais velho
    if sexo == 'M':
        if idade > MaiorIdadeHomem:
            MaiorIdadeHomem = idade
            NomeHomemMaisVelho = nome

    # 3. Conta mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        MulheresMenos20 += 1

# Média calculada fora do laço
MediaDeIdade = SomaIdade / 4

print(f'\nA média de idade do grupo é de {MediaDeIdade:.1f} anos.')

if NomeHomemMaisVelho != '':
    print(f'O homem mais velho se chama {NomeHomemMaisVelho} e tem {MaiorIdadeHomem} anos.')
else:
    print('Não foram cadastrados homens.')

print(f'Ao todo são {MulheresMenos20} mulheres com menos de 20 anos.')