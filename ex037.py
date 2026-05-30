cores = {'vermelho':'\033[0;31m',
         'azul':'\033[0;34m',
         'verde':'\033[0;32m',
         'limpa': '\033[m'}#cores pra deixar o codigo bonito

numero = int(input(f'\n{cores['azul']}Digite um numero: '))
base_conversao = int(input(f'\n{cores['verde']}"1" para binario \n"2" para octal \n"3" para hexadecial \n{cores['limpa']}{cores['azul']}Qual sera a base para conversão: '))

bin = (bin(numero))
oct = (oct(numero))
hex = (hex(numero))

if base_conversao == 1:
    print(bin)
elif base_conversao == 2:
    print(oct)
elif base_conversao == 3:
    print(hex)