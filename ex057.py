sexo = str(input('Digite o sexo da pessoa (F/M): ')).strip().upper()[0]

# O laço repete ENQUANTO o sexo NÃO ESTIVER em 'MF'
while sexo not in 'MF':
    sexo = str(input('Valor incorreto, digite novamente (F/M): ')).strip().upper()[0]

print(f'Sexo registrado com sucesso!')