d = int(input('\nDigite a distancia da sua viagem em KM: '))

if d <= 200:
    pa = (float(d)*0.5)
    print(f'\nO valor da passagem fica em: R${pa}, Boa viagem!\n')
else:
    p = (float(d)*0.45)
    print(f'\nO valor da passagem fica em: R${p}, Boa viagem!\n')