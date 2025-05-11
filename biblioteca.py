tarefas=[]

def mostrar_menu():
    print("\n===== Menu de Tarefas =====")
    print("Listar Tarefas")
    print("Inserir tarefa")
    print("Deletar tarefas")
    print("Sair")

def listar_tarefa():
    if not tarefas:
        print("Nenhuma tarefa encontrada")
    else:
        print("\nMinhas tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}.{tarefas}")

def inserir_tarefa():
    nova = input("Informe a nova tarefa: ")
    tarefas.append(nova)
    print("Nova tarefa adicionada")

def deletar_tarefa():
    listar_tarefa()
    if tarefas:
        try:
            num= int(input("Informe o número que deseja deletar: "))
            if 1<=num<= len(tarefas):
                removida = tarefas.pop(num-1)
                print(f"Tarefa {removida} deletada.")
            else:
                print("Número invalido.")
        except ValueError:
             print("Informe um número existente.")