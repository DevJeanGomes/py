from random import randint
from rich import print
from rich.traceback import install
install()

Soma = 0
VezesGanhaDoUsuarios = 0

while True:

    ValorDoUsuario = int(input('\nDigite um valor: '))
    ValorDoUsuarioImparOuPar = input('\nPar ou Impar [P?I]? ').upper()
    pc = randint(0,10)

    Soma = ValorDoUsuario + pc

    if Soma % 2 == 0 and ValorDoUsuarioImparOuPar == 'P':
        print(f'\nVoce jogou [green]{ValorDoUsuario}[/] e o pc jogou [blue]{pc}[/], [white]total[/]([red]{Soma}[/]) Deu par\n')
        print(f'[green]Voce GANHOU!\n[/]')
        print(f'Vamos jogar novamente...\n')
        VezesGanhaDoUsuarios += 1

    elif Soma % 2 != 0 and ValorDoUsuarioImparOuPar == 'I':
        print(f'\nVoce jogou [green]{ValorDoUsuario}[/] e o pc jogou [blue]{pc}[/], [white]total[/]([red]{Soma}[/]) Deu Impar\n')
        print(f'[green]Voce GANHOU!\n[/]')
        print(f'Vamos jogar novamente...\n')
        VezesGanhaDoUsuarios += 1

    else:
        print(f'\nVoce jogou [green]{ValorDoUsuario}[/] e o pc jogou [blue]{pc}[/], [white]total[/]([red]{Soma}[/]) Deu Impar\n')
        print(f'[red]Game Over, Voce PERDEU!\n[/]')
        print(f'[green]Voce venceu {VezesGanhaDoUsuarios} vezes!\n[/]')
        break
