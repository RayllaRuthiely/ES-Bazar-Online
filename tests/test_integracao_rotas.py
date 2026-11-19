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
