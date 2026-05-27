from math import sin, cos, tan, radians

a = float(input('\nDigite o valor do angulo: '))

s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('\nO angulo digitado é {}°, o seu seno é {:.2f}, o Cosseno é {:.2f}, e a Tangente é {:.2f} \n'.format(int(a),s,c,t))