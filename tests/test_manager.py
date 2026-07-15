from src.manager import GerenciadorTarefas

def test_adicionar_tarefa():
    gerenciador = GerenciadorTarefas()
    gerenciador.adicionar_tarefa("Estudar Python")

    assert len(gerenciador.tarefas) == 1
    assert gerenciador.tarefas[0].titulo == "Estudar Python"

