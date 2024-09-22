categorias = []
def adicionar(lista:list):
    lista.append({  "Nome": input("Insira o nome da tarefa: "),
                    "Prioridade": int(input("insira a prioridade desta tarefa (de 1 a 5 sendo 1 menor prioridade e 5 maior prioridade): ")),
                    "Descrição": input("insira a descrição da sua tarefa: "),
                    "Categoria": input("insira a categoria da sua tarefa: "),
                    "Feito" : False
                   })
    print("\nFeito\n")

def remover(lista):
    nome_remover = input("Insira o nome da atividade que quer remover: ")
    test = lista
    lista = list(filter(lambda atividade: atividade["Nome"] != nome_remover, lista))
    if test == lista:
        print("\nEsta atividade não está cadastrada\n")
    else:
        print("\nFeito!\n")
        return lista

def checarprio(lista:list):
    for i in sorted(lista, key=lambda x: x['Prioridade']):
        print(f"\nNome: {i['Nome']}")
        print(f"Prioridade: {i['Prioridade']}")
        print(f"Descrição: {i['Descrição']}")
        print(f"Categoria: {i['Categoria']}")
        print(f"Feito?: {'Sim' if i['Feito'] == True else 'Não'}\n")

def checarcat (lista:list):
    cat = input("Insira a categoria que deseja checar: ")
    
    encontrou = False
    for a in lista:
        if a['Categoria'] == cat:
            encontrou = True
            print(f"\nNome: {a['Nome']}")
            print(f"Prioridade: {a['Prioridade']}")
            print(f"Descrição: {a['Descrição']}")
            print(f"Categoria: {a['Categoria']}")
            print(f"Feito?: {'Sim' if a['Feito'] else 'Não'}\n")
    
    if not encontrou:
        print("\nNão tem nenhuma atividade com esta categoria\n")
                
                
        

def atualizar(lista:list):
    for i in lista:
        if i["Nome"] == input("insira o nome da atividade que deseja atualizar: "):
            print(f"\nNome:  {i['Nome']}")
            print(f"Prioridade:  {i['Prioridade']}")
            print(f"Descrição: {i['Descrição']}")
            print(f"Categoria: {i['Categoria']}")
            print(f"Feito?:  {'Sim' if i['Feito'] == True else 'Não'}\n")
            if input("deseja marcar a atividade como feita? (sim ou não): ").strip().lower() == "sim":
                i["Feito"] = True
                print("\nFeito\n")
            else:
                print("\nNenhuma alteração foi feita\n")

ativs = []

while True:
    print("~~~~Gerenciador de atividades~~~~")
    print("1 - listar atividades em ordem de prioridade")
    print("2 - listar atividades em ordem de prioridade")
    print("3 - adicionar atividade")
    print("4 - atualizar atividade")
    print("5 - excluir atividade")
    print("6 - fechar o programa\n")
    escolha = int(input("insira sua escolha: ").strip())
    print()
    
    if escolha == 1:
        if len(ativs) == 0:
            print("Nenhuma atividade adicionada ainda\n")
        else:
            checarprio(ativs)
            
    elif escolha == 2:
        if len(ativs) == 0:
            print("Nenhuma atividade adicionada ainda\n")
        else:
            checarcat(ativs)
            
    elif escolha == 3:
        adicionar(ativs)
    elif escolha == 4:
        atualizar(ativs)
    elif escolha == 5:
        ativs = remover(ativs)
    elif escolha == 6:
        print("\nAté mais <3")
        break

