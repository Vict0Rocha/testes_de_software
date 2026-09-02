from unittest.mock import Mock

import pytest

from carrinho import calcular_total


@pytest.fixture
def servico_de_precos_falso():
    servico = Mock()
    servico.buscar_preco.side_effect = lambda item: {
        "maca": 2,
        "pao": 5,
        "leite": 4,
    }[item]
    return servico


def test_calcular_total_de_um_item(servico_de_precos_falso):
    total = calcular_total(["maca"], servico_de_precos_falso)
    assert total == 2


def test_calcular_total_de_varios_itens(servico_de_precos_falso):
    total = calcular_total(["pao", "leite"], servico_de_precos_falso)
    assert total == 9


def test_calcular_total_chama_o_servico_para_cada_item(servico_de_precos_falso):
    calcular_total(["maca", "pao"], servico_de_precos_falso)
    assert servico_de_precos_falso.buscar_preco.call_count == 2
