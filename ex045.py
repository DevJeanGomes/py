import random

# Lista de opções onde o índice dita o que é o item
itens = ('Pedra', 'Papel', 'Tesoura')

# O Computador sorteia um número entre 0 e 2
computador = random.randint(0, 2)

print('=' * 25)
print('       JOKENPÔ       ')
print('=' * 25)
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

jogador = int(input('Qual é a sua jogada? '))

# Validação para o caso do jogador digitar um número inválido
if jogador < 0 or jogador > 2:
    print('\n[ERRO] Jogada inválida! Escolha entre 0, 1 ou 2.')
else:
    print('\n' + '-' * 25)
    print(f'Você jogou: {itens[jogador]}')
    print(f'O computador jogou: {itens[computador]}')
    print('-' * 25 + '\n')

    # Lógica dos Resultados
    if jogador == computador:
        print('DEU EMPATE! 🤝\n')
        
    # Condições onde o JOGADOR ganha
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print('PARABÉNS! Você VENCEU! 🎉\n')
        
    # Se não foi empate e o jogador não ganhou, o PC ganhou
    else:
        print('A MÁQUINA VENCEU! 🤖❌\n')