from rich import print

cont = 0
numeros = 0
Soma = 0

while True:
    numeros = int(input('\nDigite um valor (999 para parar): '))

    if numeros == 999:
        break

    Soma += numeros
    cont += 1

print(f'\nA soma dos [green]{cont}[/] valores foi [green]({Soma})[/]!\n')