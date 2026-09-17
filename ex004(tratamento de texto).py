# Lendo o valor pelo teclado
algo = input("Digite algo: ")

print('\nO tipo dessa variavel é: {} ' .format(type(algo)))
print('Essa variavel so tem espaco? {} ' .format(algo.isspace()))
print('É um número? {} ' .format(algo.isnumeric()))
print('É alfabético (apenas letras)? {} ' .format(algo.isalpha()))
print('É alfanumérico (letras e/ou números)? {} ' .format(algo.isalnum()))
print('Está tudo em maiúsculas? {} ' .format(algo.isupper()))
print('Está tudo em minúsculas? {} ' .format(algo.islower()))
print('Está capitalizado (com a primeira letra maiúscula)? {} ' .format(algo.istitle()))