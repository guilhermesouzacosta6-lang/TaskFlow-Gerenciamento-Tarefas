class Tarefa:
    def __init__(self, titulo):
        self.titulo = titulo
        self.concluida = False

    def concluir(self):
        self.concluida = True
        