# --------------------------Inicio das Variáveis Globais----------------------
lista_colaborador = []
id_global = 0


# --------------------------Fim das Variáveis Globais-------------------------

# --------------------------Inicio de Cadastrar Colaboradores---------------------
def cadastra_colaborador(colaborador):
    print('------------------------------MENU CADASTRAR COLABORADOR--------------------------')
    print('Id do Colaborador: {}'.format(colaborador))
    nome = input('Entre com o NOME do colaborador: ')
    setor = input('Entre com o SETOR do colaborador ')
    salario = int(input('Entre com o SALÁRIO do colaborador '))
    dicionario_produto = {'id': colaborador,
                          'nome': nome,
                          'setor': setor,
                          'salario': salario}
    lista_colaborador.append(dicionario_produto.copy())


# --------------------------Fim de Cadastrar Colaboradores---------------------

# --------------------------Inicio de Cadastrar Colaboradores---------------------
def consultar_colaborador():
    print('------------------------------MENU CONSULTAR COLABORADOR--------------------------')
    while True:
        opcao_consultar = input('1. Consultar Todos os Colaboradores\n' +
                                '2. Consultar Colaborador por id\n' +
                                '3. Consultar Colaborador(es) por setor\n' +
                                '4. Retorna\n'
                                '>>')
        if opcao_consultar == '1':
            print('Você escolheu a opção consultar TODOS os Colaboradores')
            for colaborador in lista_colaborador:
                print('-------------------------------------------------')
                for key, value in colaborador.items():
                    print('{}: {}'.format(key, value))
            print('-------------------------------------------------')
        elif opcao_consultar == '2':
            print('Você escolheu a opção consultar TODOS os Colaborador por id')
            opcao_desejado = input('Escolha a opção desejada: ')
            for colaborador in lista_colaborador:
                if colaborador['id'] == opcao_desejado:  # Se o valor for igual ao opção_desejada
                    for key, value in colaborador.items():
                        print('{}: {}'.format(key, value))
        elif opcao_consultar == '3':
            print('Você escolheu a opção consultar TODOS os Colaborador(es) por setor')
            opcao_desejado = input('Escolha a opção desejada: ')
            for colaborador in lista_colaborador:
                if colaborador['setor'] == opcao_desejado:  # Se o valor for igual ao opção_desejada
                    print('-------------------------------------------------')
                    for key, value in colaborador.items():
                        print('{}: {}'.format(key, value))
                print('-------------------------------------------------')
        elif opcao_consultar == '4':
            return  # Sair do Menu Consutar
        else:
            print('Opção inválida. Tente Novamente')
            continue  # Volta para o while True


# --------------------------Fim de Cadastrar Colaboradores---------------------

# --------------------------Inicio de Cadastrar Colaboradores---------------------
def remover_colaborador():
    print('********************************************************************************')
    print('------------------------------MENU REMOVER COLABORADOR---------------------------------')
    opcao_desejada = int(input('Digite o id do colaborador a ser removido: '))
    for colaborador in lista_colaborador:
        if colaborador['id'] == opcao_desejada:
            lista_colaborador.remove(id)


# --------------------------Fim de Cadastrar Colaboradores---------------------


# --------------------------Inicio do Main---------------------
print('Bem vindo a empresa do Erison Evangelista de Lima')
print('*****************************************************************************')
print('------------------------------MENU PRINCIPAL---------------------------------')
while True:
    opcao_Menu = input('1. Cadastrar Colaborador\n' +
                       '2. Consultar Colaborador\n' +
                       '3. Remover Colaborador\n' +
                       '4. Encerrar\n'
                       '>>')
    if opcao_Menu == '1':
        id_global = id_global + 1
        cadastra_colaborador(id_global)
    elif opcao_Menu == '2':
        consultar_colaborador()
    elif opcao_Menu == '3':
        remover_colaborador()
    elif opcao_Menu == '4':
        break
    else:
        print('Opção inválida. Tente Novamente')
        continue  # Volta para o while True
# --------------------------Fim do Main------------------------
