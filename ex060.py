from rich import print
from rich.prompt import Prompt

# Solicita o número ao usuário
numero = int(Prompt.ask('\n[bold cyan]Digite um número para calcular o Fatorial[/]'))

contador = numero
fatorial = 1

print(f'\nCalculando [yellow]{numero}![/] = ', end='')

# Laço de repetição decremental
while contador > 0:
    print(f'[cyan]{contador}[/]', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    
    fatorial *= contador  # Equivale a: fatorial = fatorial * contador
    contador -= 1         # Equivale a: contador = contador - 1

print(f'[bold green]{fatorial}[/]\n')