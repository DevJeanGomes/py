from math import hypot

c1 = float(input('\nDigite o valor do cateto oposto: '))
c2 = float(input('Digite o valor do cateto adjacente: '))
h = hypot(c1, c2)

print('O valor da hiptenusa é: {:.2f} \n'.format(h))
