lt = []
for i in range(3):
    t = float(input(f'\nDigite o valor do {i+1}º lado do triangulo: '))
    lt.append(t)

if ((lt[0] + lt[1]) > lt[2]) and ((lt[0] + lt[2]) > lt[1]) and ((lt[1] + lt[2]) > lt[0]):
    print('\nVocê pode formar um triângulo! \n')
else:
    print('\nVocê pode nao formar um triângulo! \n')
