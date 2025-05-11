from biblioteca import *

while True:
    mostrar_menu()
    opcao=input("Informe sua opção: ")

    if opcao==1:
        listar_tarefa()
    elif opcao==2:
        inserir_tarefa()
    elif opcao==3:
        deletar_tarefa()
    elif opcao==4:
        print("Você está saindo do programa.")
    else:
        print("Você digitou um número errado, por gentileza, informe uma opção existente.")