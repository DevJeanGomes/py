from rich import print
# Arquivo: funcoes.py
#from funcoes import media, maior_menor fazendo a chamada para o arquivo

def media(lista):  # funcao para o desafio 065
    # Se o último item for 0, pega do início até o penúltimo
    dados = lista[:-1] if (lista and lista[-1] == 0) else lista

    if len(dados) > 0:
        media = sum(dados) / len(dados)
        print(f"[green]A média é: {media:.2f}[/]")


def maior_menor(lista):  # funcao para o desafio 065
    # Se o último item for 0, pega do início até o penúltimo
    dados = lista[:-1] if (lista and lista[-1] == 0) else lista

    if len(dados) > 0:
        maior = max(dados)
        menor = min(dados)
        print(f"[green]Maior: {maior:.2f}[/]")
        print(f"[green]Menor: {menor:.2f}[/]")

def tabuada(numero): # funcao para o desafio 067
    resultado = 0
    for i in range(0, 11):
        resultado = numero * i
        print(f'\n{numero} x {i} = {resultado}')

