v = int(input('\nQual a velociade do carro: '))

if v > 80:
    print('\nVoce foi MULTADO! \n')
    m = (float(v) - 80.00) * 7
    print(f'A multa custa R$7.00 por Km acima do limite, voce devera pagar: R${m:.2f}\n')
else:
    print('\nVoce esta no limite permitido! \n')