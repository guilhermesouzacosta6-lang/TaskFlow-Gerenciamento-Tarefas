from src.task import Tarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, titulo):
        tarefa = Tarefa(titulo)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for indice, tarefa in enumerate(self.tarefas, start=1):
            status = "Concluída" if tarefa.concluida else "Pendente"
            print(f"{indice}. {tarefa.titulo} - {status}")

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
            return True
        return False

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas.pop(indice)
            return True
        return False
    