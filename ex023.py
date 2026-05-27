# O programa vai rodar tudo o que está aqui dentro repetidamente
while True:
    # 1. Lemos a entrada do usuário
    n = input('\nDigite um valor de 0 a 9999 (ou digite "sair" para encerrar): ').strip()
    
    # 2. Criamos uma saída de emergência se o usuário quiser encerrar
    if n.lower() == 'sair':
        print('Programa encerrado pelo usuário. Até logo!\n')
        break  # Interrompe o "while" e fecha o programa

    # 3. Fazemos a validação que você já conhece
    if n.isdigit() and 0 <= int(n) <= 9999:
        print('\nNumero valido!\n')
        
        # Executa a sua lógica de separar os dígitos
        n_atualizado = n.zfill(4)
        n_atualizado_l = list(n_atualizado)
        
        print(f'unidade: {n_atualizado_l[3]}')
        print(f'dezena:  {n_atualizado_l[2]}')
        print(f'centena: {n_atualizado_l[1]}')
        print(f'milhar:  {n_atualizado_l[0]}\n')
        
        # Como o número deu certo, usamos o break para parar o loop
        break  
        
    else:
        # Se cair no else, o "break" NÃO é executado.
        # O Python chega ao fim do bloco e volta automaticamente para o início do "while"
        print('\nNumero invalido! Tente novamente!')