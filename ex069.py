

tot18 = tot_homens = tot_mulheres_20 = 0

while True:
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        tot_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulheres_20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if resp == 'N':
        break

print(f'\n--- RESULTADO ---')
print(f'A) Pessoas com mais de 18 anos: {tot18}')
print(f'B) Homens cadastrados: {tot_homens}')
print(f'C) Mulheres com menos de 20 anos: {tot_mulheres_20}')