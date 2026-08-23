#jean carlos
# Captura a entrada do usuário, remove espaços nas pontas (.strip()) e converte para maiúsculas (.upper())
frase = str(input('Digite uma frase: ')).strip().upper()
#JEAN CARLOS

# Divide a frase em uma lista de palavras (usando os espaços entre elas como separador)
palavras = frase.split()
#JEAN CARLOS

# Agrupa todas as palavras da lista em uma única string sem espaços
junto = ''.join(palavras)
#JEANCARLOS

# Inicializa uma variável de texto vazia para acumular as letras invertidas
inverso = ''

# Laço que percorre os índices da string de trás para frente
# len(junto) - 1 : posição da última letra
# -1             : limite de parada (para alcançar o índice 0)
# -1             : passo (regressivo, voltando de 1 em 1)
for letra in range(len(junto) - 1, -1, -1):
    # Pega o caractere da posição 'letra' e adiciona ao final da variável 'inverso'
    inverso += junto[letra]
    #SOLRACNAEJ

# Exibe no terminal a palavra original sem espaços e a palavra invertida
print(f'O inverso de {junto} é {inverso}')

# Compara se a frase sem espaços é idêntica à sua versão invertida
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um palíndromo!')