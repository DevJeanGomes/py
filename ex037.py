cores = {'vermelho':'\033[0;31m',
         'azul':'\033[0;34m',
         'verde':'\033[0;32m',
         'limpa': '\033[m'}#cores pra deixar o codigo bonito

numero = int(input(f'\n{cores['azul']}Digite um numero: {cores['limpa']}'))
base_conversao = int(input(f'\n{cores['verde']}Digite "1" para binario \nDigite "2" para octal \nDigite "3" para hexadecial \n{cores['limpa']}{cores['azul']}Qual sera a base para conversão: {cores['limpa']}'))

bin = (bin(numero))
oct = (oct(numero))
hex = (hex(numero))

if base_conversao == 1:
    print(f"\n{cores['verde']}O numero {cores['limpa']}{cores['azul']}{numero}{cores['limpa']}{cores['verde']} convertido para binario é:{cores['limpa']}{cores['azul']} {bin}\n{cores['limpa']}")
elif base_conversao == 2:
    print(f"\n{cores['verde']}O numero {cores['limpa']}{cores['azul']}{numero}{cores['limpa']}{cores['verde']} convertido para octal é:{cores['limpa']}{cores['azul']} {oct}\n{cores['limpa']}")
elif base_conversao == 3:
    print(f"\n{cores['verde']}O numero {cores['limpa']}{cores['azul']}{numero}{cores['limpa']}{cores['verde']} convertido para hexadecimal é:{cores['limpa']}{cores['azul']} {hex}\n{cores['limpa']}")