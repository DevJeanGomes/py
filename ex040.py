cores = {'vermelho':'\033[0;31m',
         'azul':'\033[0;34m',
         'verde':'\033[0;32m',
         'limpa': '\033[m'}#cores pra deixar o codigo bonito

nota_1 = float(input('\nDigite o valor da sua primeria nota: '))
nota_2 = float(input('\nDigite o valor da sua primeria nota: '))
media = (nota_1 + nota_2)/2

if media < 5:
    print(f'{cores['vermelho']}\nREPROVADO\n{cores['limpa']}')
elif media >= 5.0 and media <= 6.9:
    print(f'{cores['azul']}\nRECUPERAÇAO\n{cores['limpa']}')
else:
    print(f'{cores['verde']}\nAPROVADO\n{cores['limpa']}')