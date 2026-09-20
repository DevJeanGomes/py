from random import randint
from rich import print

tupla_numeros = tuple(randint(1, 100) for _ in range(5))

maior = max(tupla_numeros)
menor = min(tupla_numeros)

print(f"\nOs valores sorteados foram: [green]{tupla_numeros}[/]")
print(f"\nO maior numero é [green]{maior}[/]")
print(f"\nO menor numero é [green]{menor}[/]\n")