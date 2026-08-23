soma = 0

for contador in range(1,7):
    NumeroDoUsuario = int(input(f'Digite o {contador}º: '))
    if NumeroDoUsuario % 2 == 0:
        soma += NumeroDoUsuario
 
print(f'\nA soma dos valores pares sao: {soma}\n')  
     
print('fim\n')
