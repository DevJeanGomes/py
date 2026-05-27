ano = int(input('\nDigite um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('\nO ano é bissexto!\n')
else:
    print('\nO ano nao é bissexto!\n')