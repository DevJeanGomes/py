total_gasto = tot_mais_1000 = menor_preco = cont = 0
produto_mais_barato = ''

while True:
    produto = input('Nome do produto: ').strip()
    preco = float(input('Preço: R$ '))
    
    cont += 1
    total_gasto += preco

    if preco > 1000:
        tot_mais_1000 += 1

    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_mais_barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    
    if resp == 'N':
        break

print(f'\n--- RESULTADO ---')
print(f'A) Total gasto na compra: R$ {total_gasto:.2f}')
print(f'B) Produtos que custam mais de R$ 1000.00: {tot_mais_1000}')
print(f'C) Produto mais barato: {produto_mais_barato} (R$ {menor_preco:.2f})')