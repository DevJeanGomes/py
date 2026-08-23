numero = int(input('Digite um valor: '))
ContadorDeDivisores = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        ContadorDeDivisores += 1

if ContadorDeDivisores == 2:
    print('É um número PRIMO!')
else:
    print('NÃO é um número PRIMO!')