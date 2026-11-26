import io

import pytest
import routes.anuncio as rota_anuncio
from routes.anuncio import validar_anuncio

CATEGORIAS = [
    {"ID_CATEGORIA": 1, "NOME_CATEGORIA": "Roupas"},
    {"ID_CATEGORIA": 2, "NOME_CATEGORIA": "Calçados"},
]
IDS = {1, 2}


# ---------- Regras do anúncio (unidade) ----------


def test_aceita_anuncio_valido():
    erros = validar_anuncio("Camiseta", "Pouco usada", "20.00", "1", "foto.jpg", IDS)
    assert erros == []


@pytest.mark.parametrize(
    "titulo, preco, categoria, foto",
    [
        ("", "20", "1", "foto.jpg"),
        ("Camiseta", "", "1", "foto.jpg"),
        ("Camiseta", "20", "", "foto.jpg"),
        ("Camiseta", "20", "1", ""),
    ],
)
def test_recusa_campos_obrigatorios_vazios(titulo, preco, categoria, foto):
    erros = validar_anuncio(titulo, "", preco, categoria, foto, IDS)
    assert erros == ["Preencha os dados obrigatórios do anúncio"]


@pytest.mark.parametrize(
    "preco, valido",
    [("-1", False), ("0", False), ("0.01", True), ("10,50", True), ("abc", False)],
)
def test_preco_valores_limite(preco, valido):
    erros = validar_anuncio("Camiseta", "", preco, "1", "foto.jpg", IDS)
    assert (erros == []) is valido


def test_recusa_categoria_inexistente():
    erros = validar_anuncio("Camiseta", "", "20", "99", "foto.jpg", IDS)
    assert "Escolha uma categoria válida" in erros


def test_recusa_foto_com_extensao_invalida():
    erros = validar_anuncio("Camiseta", "", "20", "1", "virus.exe", IDS)
    assert "A foto deve ser JPG, JPEG, PNG ou WEBP" in erros


def test_recusa_titulo_maior_que_50_caracteres():
    erros = validar_anuncio("a" * 51, "", "20", "1", "foto.jpg", IDS)
    assert "O título deve ter até 50 caracteres" in erros


# ---------- Rota /novo-anuncio (integração, com banco falso) ----------


class CursorFalso:
    def __init__(self, banco):
        self.banco = banco
        self.lastrowid = None

    def execute(self, sql, valores=None):
        self.banco.comandos.append((sql, valores))
        if "INSERT INTO ANUNCIO" in sql:
            self.lastrowid = 7

    def fetchall(self):
        return CATEGORIAS

    def close(self):
        pass


class BancoFalso:
    def __init__(self):
        self.comandos = []
        self.confirmado = False

    def cursor(self, dictionary=False):
        return CursorFalso(self)

    def commit(self):
        self.confirmado = True

    def rollback(self):
        pass

    def close(self):
        pass


@pytest.fixture
def banco(monkeypatch, tmp_path):
    banco_falso = BancoFalso()
    monkeypatch.setattr(rota_anuncio, "conectar_banco", lambda: banco_falso)
    from app import app

    monkeypatch.setattr(app, "static_folder", str(tmp_path))
    return banco_falso


def test_formulario_mostra_categorias_do_banco(client, banco):
    resposta = client.get("/novo-anuncio")
    assert resposta.status_code == 200
    assert "Calçados" in resposta.get_data(as_text=True)


def test_publica_anuncio_e_foto_na_mesma_transacao(client, banco):
    dados = {
        "titulo": "Camiseta",
        "descricao": "Pouco usada",
        "preco": "20",
        "categoria": "1",
        "foto": (io.BytesIO(b"imagem"), "camiseta.jpg"),
    }
    resposta = client.post(
        "/novo-anuncio", data=dados, content_type="multipart/form-data"
    )

    assert resposta.status_code == 201
    assert "Anúncio publicado com sucesso" in resposta.get_data(as_text=True)
    sqls = [sql for sql, _ in banco.comandos]
    assert any("INSERT INTO ANUNCIO" in sql for sql in sqls)
    assert any("INSERT INTO FOTO" in sql for sql in sqls)
    assert banco.confirmado


def test_recusa_anuncio_incompleto_sem_gravar(client, banco):
    dados = {"titulo": "Camiseta", "preco": "", "categoria": "1"}
    resposta = client.post(
        "/novo-anuncio", data=dados, content_type="multipart/form-data"
    )

    assert resposta.status_code == 422
    texto = resposta.get_data(as_text=True)
    assert "Preencha os dados obrigatórios do anúncio" in texto
    assert 'value="Camiseta"' in texto  # mantém o que já foi preenchido
    assert not banco.confirmado
