from datetime import datetime

ano = int(input('\nDigite o ano em que voce nasceu: '))

idade = datetime.now().year - ano
faltam = 18 - idade
passou = idade - 18

if idade < 18:
    print(f'\nFaltam {faltam} anos para voçe ainda se alistar no serviço militar.\n')
elif idade == 18:
    print(f'\nEsta na hora de voçe deve se alistar ao serviço militar.\n')
else:
    print(f'\nJa passou {passou} anos da hora de voçe se alistar.\n')
