frase = input('\nDigite a frase: ').strip()

print('\nA letra "A" apareceu {} vezes, a primeira pociçao que ela apareceu foi a pociçao {}, e a ultima foi a pociçao {}\n'.format(frase.upper().count('A'),frase.upper().find('A'),frase.upper().rfind('A')))