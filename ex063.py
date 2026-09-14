from rich import print

n = int(input('\nQuantos termos de fibonnaci voce quer ver: '))

t1, t2 = 0, 1
contador = 0

while contador != n:
    print(t1, end=" -> " if contador < n - 1 else "\n")
    t1, t2 = t2, t1 + t2
    contador += 1
    