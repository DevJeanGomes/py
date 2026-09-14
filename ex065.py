from rich import print
from funcoes import media, maior_menor

Numeros = []
contador = True
cont = 1

print(f'\n[red]Digite (0) para PARAR o programa quando quiser![/]')
while contador:

    Valor = int(input(f'Digite o {cont}º valor: '))
    Numeros.append(Valor)
    cont+=1

    if Valor == 0:
        media(Numeros)
        maior_menor(Numeros)
        contador = False
