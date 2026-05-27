nome = input('\nDigite seu nome: ').strip()

v = nome.upper().find("SILVA")

if v >= 0:
    print('\nSeu nome tem silva!\n')
else:
    print('\nseu nome nao tem silva!\n')
