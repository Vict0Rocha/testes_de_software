import pytest

from repositorio_tarefas import RepositorioTarefas
from servico_tarefas import ServicoTarefas


@pytest.fixture
def servico():
    repositorio = RepositorioTarefas()
    return ServicoTarefas(repositorio)


def test_adicionar_tarefa_aparece_na_lista(servico):
    servico.adicionar("lavar louça")

    pendentes = servico.pendentes()

    assert len(pendentes) == 1
    assert pendentes[0]["titulo"] == "lavar louça"


def test_concluir_tarefa_nao_aparece_nas_pendentes(servico):
    tarefa = servico.adicionar("estudar")

    servico.concluir(tarefa["id"])

    assert len(servico.pendentes()) == 0


def test_adicionar_duas_tarefas_mantem_a_ordem(servico):
    servico.adicionar("primeira")
    servico.adicionar("segunda")

    pendentes = servico.pendentes()

    assert len(pendentes) == 2
    assert pendentes[0]["titulo"] == "primeira"
    assert pendentes[1]["titulo"] == "segunda"


def test_concluir_tarefa_que_nao_existe_da_erro(servico):
    with pytest.raises(ValueError):
        servico.concluir(999)
