class RepositorioTarefas:
    def __init__(self):
        self.tarefas = []

    def salvar(self, tarefa):
        self.tarefas.append(tarefa)

    def listar(self):
        return self.tarefas

    def buscar(self, id):
        for tarefa in self.tarefas:
            if tarefa["id"] == id:
                return tarefa
        raise ValueError("tarefa não encontrada")
