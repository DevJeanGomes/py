from datetime import datetime

ano = int(input('\nDigite o ano em que voce nasceu: '))

idade = datetime.now().year - ano

if idade <= 9:
    print('\nA sua categoria é MIRIM\n')
elif idade <= 14:
    print('\nA sua categoria é INFANTIL\n')
elif idade <= 19:
    print('\nA sua categoria é JUNIOR\n')
elif idade <= 20:
    print('\nA sua categoria é SENIOR\n')
else:
    print('\nA sua categoria é MASTER\n')