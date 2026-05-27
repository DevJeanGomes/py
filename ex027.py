n = input('\nDigite seu nome completo: ').strip()

nome = n.split()

print('\nSeu primeiro nome é: "{}" e seu ultimo nome é: "{}"\n'.format(nome[0],nome[-1]))