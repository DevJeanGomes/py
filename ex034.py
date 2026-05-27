salario = float(input('\nDigite seu salario: '))

if salario >= 1250:
    salario_1 = salario * 1.10
    print(f'\nSeu salario com aumento sera de R${salario_1:.2f} \n')
else:
    salario_2 = salario * 1.15
    print(f'\nSeu salario com aumento sera de R${salario_2:.2f} \n')