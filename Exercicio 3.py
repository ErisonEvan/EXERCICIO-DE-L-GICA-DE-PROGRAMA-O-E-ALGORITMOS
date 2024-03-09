def cachorro_peso():
    global peso
    while True:
        try:
            peso = int(input('Entre com o peso do cachorro: '))
            if peso < 3:
                return 10
            elif 3 >= peso < 10:
                return 50
            elif 10 <= peso < 30:
                return 60
            elif 30 <= peso < 50:
                return 70
            elif peso > 50:
                print('Não aceitamos cachorros tão grandes')
                print('Por favor entre com o peso do cachorro novamente.\n')
                continue
        except ValueError:
            print('Voce digitou um valor não numérico')
            print('Por favor entre com o peso do cachorro novamente.\n')


def cachorro_pelo():
    global pelo
    while True:
        pelo = input('Entre com o pelo do cachorro\n'
                     'c - Pelo Curto\n'
                     'm - Pelo Médio\n'
                     'l - Pelo Longo\n'
                     '>>')
        pelo = pelo.lower()
        pelo = pelo.strip()
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        continue


def cachorro_extra():
    global extra
    acumulador = 0
    while True:
        extra = input('Deseja acionar mais algum serviço?\n'
                      '1 - Corte de Unhas - R$ 10,00  \n' +
                      '2 - Escovar Dentes  - R$ 12,00 \n' +
                      '3 - Limpeza de Orelhas - R$ 15,00 \n' +
                      '0 - Não desejo mais nada \n' +
                      '>>')
        print('\n')
        if extra == '0':
            return acumulador + 0
        elif extra == '1':
            acumulador = acumulador + 10
            continue
        elif extra == '2':
            acumulador = acumulador + 12
            continue
        elif extra == '3':
            acumulador = acumulador + 15
            continue
        else:
            print('Pare de digitar opções diferentes de 0/1/2/3')
        continue


print('Seja Bem vindo ao appshop, desenvolvido por Erison Evangelista de Lima')
print('\n')4
peso = cachorro_peso()
print('\n')
pelo = cachorro_pelo()
print('\n')
extra = cachorro_extra()
total = peso * pelo + extra
print('\n')
print('Total a pagar(R$): {:.2f} (peso {} * pelo: {} + adicional(is): {})'.format(total, peso, pelo, extra))
