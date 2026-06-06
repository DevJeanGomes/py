peso = float(input('\nDigite seu peso: '))
altura = float(input('\nDigite sua altura: '))
imc = peso / (pow(altura, 2))

if imc < 18.5:
    print('\nAbaixo do peso. \n')
elif imc <= 25:
    print('\nVoce esta com peso ideal. \n')
elif imc <= 30:
    print('\nVoce esta com sobrepeso. \n')
elif imc <= 40:
    print('\nVoce esta com obesidade. \n')
else:
    print('\nVoce esta com obesidade morbida. \n')