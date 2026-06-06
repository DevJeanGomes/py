preco = float(input('\nDigite o preço do produto: R$'))
linha = '='*25
print(f'\n{linha}FORMAS DE PAGAMENTO{linha}\n\nDigite o numero "1" para à vista dinheiro/cheque: 10% de desconto.\nDigite o numero "2" para à vista no cartão: 5% de desconto.\nDigite o numero "3" em até 2x no cartão: preço normal.\nDigite o numero "4" em 3x ou mais no cartão: 20% de juros. ')
condicao_pagamento = input('\nDigite a forma de pagameto: ')

if condicao_pagamento == '1':
    c1 = preco * 0.90
    print(f'\no o preço do produto é R${preco}, à vista dinheiro/cheque: 10% de desconto fica em: R${c1} \n')

elif condicao_pagamento == '2':
    c2 = preco * 0.95
    print(f'\no o preço do produto é R${preco}, à vista no cartão: 5% de desconto fica em: R${c2} \n')

elif condicao_pagamento == '3':
    c3 = preco
    print(f'\no o preço do produto é R${preco}, em até 2x no cartão: preço normal fica em: R${c3} \n')

elif condicao_pagamento == '4':
    c4 = preco * 1.20
    print(f'\no o preço do produto é R${preco}, 3x ou mais no cartão: 20% de juros fica em: R${c4} \n')
