# 1. Recebendo 4 valores e guardando na tupla (como vimos no método 2)
valores = tuple(int(input(f"Digite o {i+1}º valor: ")) for i in range(4))

# A) Quantas vezes apareceu o valor 9
quantidade_noves = valores.count(9)
print(f"\nO valor 9 apareceu {quantidade_noves} vez(es).")

# B) Em que posição foi digitado o primeiro valor 3
if 3 in valores:
    # Soma-se 1 porque o índice em Python começa no zero
    posicao_tres = valores.index(3) + 1 
    print(f"O primeiro valor 3 foi digitado na {posicao_tres}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

# C) Quais foram os números pares
print("Os números pares digitados foram: ", end="\n")
for numero in valores:
    if numero % 2 == 0:
        print(numero, end=" ")
print() # Apenas para pular uma linha no final