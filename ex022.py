nome_completo = input('\nDigite seu nome completo: ').strip()

print(f'\nO nome digitado foi: {nome_completo}, e o nome com todas as letras maiúsculas é: {nome_completo.upper()}')
print(f'\nO nome digitado foi: {nome_completo}, e o nome com todas as letras minúsculas é: {nome_completo.lower()}')

total_letras = len("".join(nome_completo.split()))
print(f'\nO nome digitado foi: {nome_completo}, e a quantidade de letras sem considerar espaços é: {total_letras}')

nome_s = nome_completo.split(" ")
print(f'\nO nome digitado foi: {nome_completo}, e a quantidade de letras que tem o primeiro nome é: {len(nome_s[0])}\n')