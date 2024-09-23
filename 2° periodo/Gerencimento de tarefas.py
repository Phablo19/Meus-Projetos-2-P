lista_de_tarefas = []
tarefas = {}
lista_de_filtragem = []
def adicionar_tarefa():
    status = []
    prioridade = []
    id = len(lista_de_tarefas) + 1
    descricao = input(' Informe a descrição da tarefa: ')
    opcao = input('Status da tarefa | 1.Pendente | 2.em andamento | 3. concluida: ')
    if opcao == "1":
        status.append("Pendente")
    elif opcao == "2":
        status.append("em andamento")
    elif opcao =="3":
        status.append("Concluida")
    
    opcao_prioridade = input('prioridade da tarefa 1.Alta | 2.media | 3.baixa: ')
    if opcao_prioridade == "1":
        prioridade.append('Alta')
    elif opcao_prioridade == "2":
        prioridade.append('media')
    elif opcao_prioridade == "3":
        prioridade.append("baixa")

    tarefas = {
        "id": id,
        "Descrição": descricao,
        "status": status,
        "Prioridade": prioridade}
    lista_de_tarefas.append(tarefas)

def visualizar_tarefa():
    for tarefa in lista_de_tarefas:
        print(f'id:{tarefa["id"]} | Descrição:{tarefa["Descrição"]} | Status:{tarefa["status"]} | Prioridade:{tarefa["Prioridade"]}\n')
    if len(lista_de_tarefas) == 0:
        print('Lista vazia\n')

def filtrar_tarefa():
    status = input('Insira o status da(s) tarefa(s) que deseja filtrar (pendente, em andamento, concluída): ')
    prioridade = input('Insira a prioridade da(s) tarefa(s) que deseja filtrar (alta, média, baixa): ')
    for tarefas in lista_de_tarefas:
        if tarefas['status'] == status and tarefas['Prioridade'] == prioridade:
            lista_de_filtragem.append(tarefas)
    if lista_de_filtragem:
        print('Tarefas filtradas:')
        for tarefas in lista_de_filtragem:
            print(tarefas)
    else:
        print("nada encotrado")    
def menu():
    while True:
        print('1. Adicionar tarefa')
        print('2. Visualizar tarefa')
        print('3. Filtrar tarefas')
        print('4. Encerrar sistema')

        opcao = input('Selecione uma das opções acima: ')
        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            visualizar_tarefa()
        elif opcao == '3':
            filtrar_tarefa()
        else:
            print("Opção invalida!\n")
menu()