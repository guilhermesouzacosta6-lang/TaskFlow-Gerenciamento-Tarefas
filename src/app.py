from src.manager import GerenciadorTarefas

def menu():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n=== TaskFlow ===")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Título da tarefa: ")
            gerenciador.adicionar_tarefa(titulo)

        elif opcao == "2":
            gerenciador.listar_tarefas()

        elif opcao == "3":
            indice = int(input("Número da tarefa: ")) - 1
            gerenciador.concluir_tarefa(indice)

        elif opcao == "4":
            indice = int(input("Número da tarefa: ")) - 1
            gerenciador.remover_tarefa(indice)

        elif opcao == "5":
            print("Encerrando...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()