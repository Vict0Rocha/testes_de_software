class ServicoTarefas:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def adicionar(self, titulo):
        id = len(self.repositorio.listar()) + 1
        tarefa = {"id": id, "titulo": titulo, "concluida": False}
        self.repositorio.salvar(tarefa)
        return tarefa

    def concluir(self, id):
        tarefa = self.repositorio.buscar(id)
        tarefa["concluida"] = True

    def pendentes(self):
        lista = []
        for tarefa in self.repositorio.listar():
            if tarefa["concluida"] == False:
                lista.append(tarefa)
        return lista
