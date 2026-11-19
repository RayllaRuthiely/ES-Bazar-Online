import pytest


def validar_dados_anuncio(titulo: str, descricao: str, preco: float) -> bool:
    if not titulo or not titulo.strip():
        return False
    if not descricao or not descricao.strip():
        return False
    if preco <= 0:
        return False
    return True


@pytest.mark.parametrize(
    "preco, esperado",
    [
        (-10.00, False),  # Partição inválida
        (-0.01, False),  # Valor limite inferior inválido
        (0.01, True),  # Valor limite inferior válido
        (50.00, True),  # Partição válida típica
    ],
)
def test_validar_preco_anuncio_valores_limite(preco, esperado):
    # Preparar / Agir
    resultado = validar_dados_anuncio("Bicicleta Aro 29", "Em ótimo estado", preco)

    # Conferir
    assert resultado is esperado


def test_recusa_anuncio_com_campos_obrigatorios_vazios():
    # Preparar / Agir
    resultado = validar_dados_anuncio("", "Descrição válida", 25.00)

    # Conferir
    assert resultado is False
