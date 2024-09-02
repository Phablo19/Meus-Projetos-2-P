def adicionar_cliente(clientes):
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    clientes.append([nome, email, telefone, endereco])
    print("Cliente adicionado com sucesso!")

def exibir_clientes(clientes):
    if len(clientes) == 0:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")

def buscar_cliente(clientes):
    email = input("Digite o e-mail do cliente: ")
    for cliente in clientes:
        if cliente[1] == email:
            print(f"Cliente encontrado: Nome: {cliente[0]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
            return
    print("Cliente não encontrado.")

def remover_cliente(clientes):
    email = input("Digite o e-mail do cliente a ser removido: ")
    for cliente in clientes:
        if cliente[1] == email:
            clientes.remove(cliente)
            print("Cliente removido com sucesso!")
            return
    print("Cliente não encontrado.")

clientes = []
while True:
    print("\n1. Adicionar Cliente")
    print("2. Exibir Clientes")
    print("3. Buscar Cliente por E-mail")
    print("4. Remover Cliente")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        adicionar_cliente(clientes)
    elif opcao == '2':
        exibir_clientes(clientes)
    elif opcao == '3':
        buscar_cliente(clientes)
    elif opcao == '4':
        remover_cliente(clientes)
    elif opcao == '5':
        print("Encerrando o sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")