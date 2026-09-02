from boliche import calcular_pontuacao


def test_partida_sem_derrubar_pinos_soma_zero():
    jogadas = [0] * 20
    assert calcular_pontuacao(jogadas) == 0


def test_jogadas_normais_somam_os_pinos():
    jogadas = [1] * 20
    assert calcular_pontuacao(jogadas) == 20


def test_spare_soma_bonus_da_proxima_jogada():
    jogadas = [5, 5, 3] + [0] * 17
    assert calcular_pontuacao(jogadas) == 16


def test_strike_soma_bonus_das_duas_proximas_jogadas():
    jogadas = [10, 4, 3] + [0] * 16
    assert calcular_pontuacao(jogadas) == 24


def test_jogo_perfeito_soma_trezentos():
    jogadas = [10] * 12
    assert calcular_pontuacao(jogadas) == 300
