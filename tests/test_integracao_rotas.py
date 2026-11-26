def test_rota_cadastro_exibe_formulario(client):
    # Agir
    resposta = client.get("/cadastro")

    # Conferir
    assert resposta.status_code == 200


def test_rota_inexistente_retorna_not_found(client):
    # Agir
    resposta = client.get("/rota-que-nao-existe")

    # Conferir
    assert resposta.status_code == 404


def test_pagina_inicial_redireciona_para_cadastro(client):
    # Agir
    resposta = client.get("/")

    # Conferir
    assert resposta.status_code == 302
    assert "/cadastro" in resposta.headers["Location"]
