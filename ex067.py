from funcoes import tabuada
from rich import print

numero = 0

while True:
    numero = int(input('\nQuer ver a tabuada de qual valor (digite qualquer valor negativo pra sair): '))
    if numero < 1:
        break
    tabuada(numero)