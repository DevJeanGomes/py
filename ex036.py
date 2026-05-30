cores = {'vermelho':'\033[0;31m',
         'azul':'\033[0;34m',
         'verde':'\033[0;32m',
         'limpa': '\033[m'}#cores pra deixar o codigo bonito

valor_casa = float(input(f'\n{cores['azul']}Qual sera o valor da casa: R$'))
#variavel para saber o valor da casa

salario = float(input(f'\n{cores['azul']}Qual é o seu salario: R$'))
#variavel para saber o salario

# Cálculos
anos_pagar = float(input(f'\n{cores['azul']}Em quantos anos voce ira pagar: '))#varial para saber quantos anos ele vai pagar a casa
prestacao = valor_casa / (anos_pagar * 12)#variavel para calcular o prestaçao da casa

salario_30 = salario * 0.30
#varial para calcuar 30% do salrio

if prestacao > salario_30:
    #se a prestaçao for maior q 30% do salrio ele nega o emprestimo
    print(f'\n{cores['vermelho']}Emprestimo negado! {cores['limpa']}\n')
else:
    #se for menor ele aprova
    print(f'\n{cores['verde']}Emprestimo aprovado! {cores['limpa']}\n')

