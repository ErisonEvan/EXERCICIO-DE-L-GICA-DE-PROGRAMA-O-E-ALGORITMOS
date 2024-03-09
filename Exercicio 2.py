print('Bem-vindo a sorveteria do Erison Evangelista de Lima')

print('-------------------------------------Cardápio-------------------------------------')
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es)|')
print('|      1      |         R$ 6,00        |      R$ 7,00       |       R$ 8,00      |')
print('|      2      |         R$ 11,00       |      R$ 13,00      |       R$ 15,00     |')
print('|      3      |         R$ 15,00       |      R$ 18,00      |       R$ 21,00     |')
print("----------------------------------------------------------------------------------\n")
acumulador = 0

while True:
    sabor = input('Entre com o sabor desejado (tr/pr/es): ') # Pedindo para o cliente digitar o sabor do sorvete.
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Sabor inválido. Tente novamente\n')
        continue #Caso o cliente digite um valor invalido ele ficarar preso nessa ação ate acerta.

    n_bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')# Pedindo para o cliente digitar o número de bolas.
    if n_bolas != '1' and n_bolas != '2' and n_bolas != '3':
        print('Número de bolas de sorvete inválido. Tente novamente\n')
        continue    #Caso o cliente digite um valor invalido ele retornara novamente para o começo do while.

    if n_bolas == '1' and sabor == 'tr':#n_bolas que é o numero de bolas é igual a '1' e sabor 'tr' igual a Tradicional.
        print('Você pediu 1 bola de sorvete no sabor TRADICIONAL: R$ 6,00')#Mostrara na tela uma mensagem do pedido.
        acumulador = acumulador + 6 #Farar a ação de pegar o valor tinha no acumulador e somar com  6.

    elif n_bolas == '2' and sabor == 'tr':
        print('Você pediu 2 bola de sorvete no sabor TRADICIONAL: R$ 11,00')
        acumulador = acumulador + 11

    elif n_bolas == '3' and sabor == 'tr':
        print('Você pediu 3 bola de sorvete no sabor TRADICIONAL: R$ 15,00')
        acumulador = acumulador + 15

    elif n_bolas == '1' and sabor == 'pr':
        print('Você pediu 1 bola de sorvete no sabor PREMIUM: R$ 7,00')
        acumulador = acumulador + 7

    elif n_bolas == '2' and sabor == 'pr':
        print('Você pediu 2 bola de sorvete no sabor PREMIUM: R$ 13,00')
        acumulador = acumulador + 13

    elif n_bolas == '3' and sabor == 'pr':
        print('Você pediu 3 bola de sorvete no sabor PREMIUM: R$ 18,00\n')
        acumulador = acumulador + 18

    elif n_bolas == '1' and sabor == 'es':
        print('Você pediu 1 bola de sorvete no sabor ESPECIAL: R$ 8,00')
        acumulador = acumulador + 8

    elif n_bolas == '2' and sabor == 'es':
        print('Você pediu 2 bola de sorvete no sabor ESPECIAL: R$ 15,00')
        acumulador = acumulador + 15

    elif n_bolas == '3' and sabor == 'es':
        print('Você pediu 3 bola de sorvete no sabor ESPECIAL: R$ 21,00')
        acumulador = acumulador + 21

    outro_sv = input('Deseja mais algum sorvete (s/digite outra tecla)?: ') #Perguntara se o cliente deseja escolher outro sorvete.
    print('\n')
    if outro_sv == 's':#Caso o cliente digite 's', retornara para o começo do while
        continue
    else:
        print('O valor total a ser pago: R${:.2f}.'.format(acumulador))#Caso o cliente digite qualquer tecla, mostrara na tela o valor total da compra.]
        break