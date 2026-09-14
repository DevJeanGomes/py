from rich import print


def SomaDaLista(lista):
    ignorar = 999
    # Filtra e soma apenas os valores diferentes de 999
    total = sum(num for num in lista if num != ignorar)
    quantidade = sum(1 for num in lista if num != ignorar)

    print(f"Quantidade digitada (sem o 999): {quantidade}")
    print(f"Soma total: {total}")


Numeros = []
contador = 0

while True:
    print('\n[red]Digite "999" para parar![/]')
    valor = int(input(f"\nDigite o {contador + 1}º valor: "))

    Numeros.append(valor)

    if valor == 999:
        SomaDaLista(Numeros)
        break

    contador += 1