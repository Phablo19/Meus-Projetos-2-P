clientes = {}

def adicionar_cliente():
    email = input("Digite o seu email: ")
    if email in clientes:
        print("Cliente já cadastrado!")
    else:
        nome = input("Informe o nome do usuário: ")
        telefone = input('Digite o telefone do cliente: ')
        endereco = input("Digite o endereço do cliente: ")

        clientes[email] = {
            'Nome': nome,
            'Email': email,
            'Telefone': telefone,
            'Endereço': endereco
        }
        print(f'Cliente {nome} registrado com sucesso!')

def exibir_clientes():
    for cliente in clientes.values():
        print(cliente)
    print("Cliente não encotrado")
    
def buscar_cliente():
    email = input('Informe o email do cliente: ')
    if email in clientes:
        cliente = clientes[email]
        print(f'Nome: {cliente['Nome']}')
        print(f'Email: {cliente['Email']}')
        print(f'Endereço: {cliente['Endereço']}')
        print(f'Telefone: {cliente['Telefone']}')
    else:
        print('Cliente não registrado:')


def remover_cliente():
    email = input("Digite o e-mail do cliente a ser removido: ")
    if email in clientes:
            del clientes[email]
            print("Cliente removido com sucesso!")
    else:
        print("Cliente não encontrado.")


while True:
    print("\n1. Adicionar Cliente")
    print("2. Exibir Clientes")
    print("3. Buscar Cliente por E-mail")
    print("4. Remover Cliente")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    print()

    if opcao == '1':
        adicionar_cliente()
    elif opcao == '2':
        exibir_clientes()
    elif opcao == '3':
        buscar_cliente()
    elif opcao == '4':
        remover_cliente()
    elif opcao == '5':
        print("Encerrando o sistema.")
        break
    else:
       print("Opção indisponivel. Tente novamente.")
