from rich import print

def Somar(Numero_1, Numero_2):
    resultado = Numero_1 + Numero_2
    print(f'[green]\n{Numero_1} + {Numero_2} = {resultado:.2f}\n[/]')

def Multiplicar(Numero_1, Numero_2):
    resultado_multiplicacao = Numero_1 * Numero_2
    print(f'[green]\n{Numero_1} x {Numero_2} = {resultado_multiplicacao:.2f}\n[/]')

def Maior(Numero_1, Numero_2):
    if Numero_1 > Numero_2:
        print(f'[green]\no maior numero entre {Numero_1} e {Numero_2} é {Numero_1:.2f}\n[/]')
    elif Numero_1 == Numero_2:
        print(f'[green]\no numero {Numero_1:.2f} e {Numero_2:.2f} sao iguais!\n[/]')
    else:
        print(f'[green]\no maior numero entre {Numero_1} e {Numero_2} é {Numero_2:.2f}\n[/]')

def DoisValores():

    Numero_1 = float(input(f'\nDigite o primeiro numero: '))
    Numero_2 = float(input(f'\nDigite o segundo numero: '))

    opcao = 0

    while opcao != 5:

        print(f'\n[1]somar\n[2]multiplciar\n[3]maior\n[4]novos numero\n[5]sair do programa\n')

        escolha = int(input(f'Digite qual opcao vc deseja: '))

        if escolha == 1:
            Somar(Numero_1, Numero_2)
            opcao = 5
        elif escolha == 2:
            Multiplicar(Numero_1, Numero_2)
            opcao = 5
        elif escolha == 3:
            Maior(Numero_1, Numero_2)
            opcao = 5   
        elif escolha == 4:
            print('\n--- Digite os novos valores ---')
            Numero_1 = float(input('Digite o primeiro número: '))
            Numero_2 = float(input('Digite o segundo número: '))
        else:
            opcao = 5

    print(f'[red]voce saiu do programa!\n[/]')
        
DoisValores()

