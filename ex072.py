from rich import print

Numeros = ('zero','um','dois', 'tres','quatro','cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quartorze','quinze','dezesseis','dezessete',
           'dezoito','dezenove','vinte')\

NumeroDoUsuario = int(input('\nDigite um valor entre (0 e 20): '))

while NumeroDoUsuario < 0 or NumeroDoUsuario > 20:
    NumeroDoUsuario = int(input('\nValor invalido, digite um valor entre (0 e 20): '))
print(f'\nO valor digitado foi [green]{Numeros[NumeroDoUsuario]}\n[/]')
    
