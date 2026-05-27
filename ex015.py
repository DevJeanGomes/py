dias = int(input('Quantos dias ele foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

preco = (km*0.15)+(dias*60)

print('Total a pagar é R${:.2f}'.format(preco))

