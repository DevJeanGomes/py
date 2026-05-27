
ln = []

for contador in range(3):
    j = float(input(f'\nDigite o {contador+1}º numero: '))
    ln.append(j)

print(f'\nO maior numero é ({max(ln)}) e o menor numero é ({min(ln)})\n')
