import os
import uuid
from datetime import datetime

from database.db import conectar_banco
from flask import Blueprint, current_app, render_template, request, session

anuncio = Blueprint("anuncio", __name__)

# Limites iguais aos das colunas da tabela ANUNCIO
TAMANHO_MAXIMO_TITULO = 50
TAMANHO_MAXIMO_DESCRICAO = 100
EXTENSOES_PERMITIDAS = {"jpg", "jpeg", "png", "webp"}
STATUS_INICIAL = "Disponível"  # RN-02

# TODO (João Guilherme): trocar pelo usuário da sessão quando o login (Alana)
# estiver na main. Até lá, todo anúncio é publicado pelo usuário de id 1.
ID_USUARIO_TEMPORARIO = 1


def validar_anuncio(
    titulo, descricao, preco_texto, id_categoria, nome_foto, ids_categorias
):
    """Regras do anúncio (HU-02, CA-01.2, RN-01). Devolve a lista de erros."""
    erros = []

    if not titulo or not preco_texto or not id_categoria or not nome_foto:
        erros.append("Preencha os dados obrigatórios do anúncio")
        return erros

    if len(titulo) > TAMANHO_MAXIMO_TITULO:
        erros.append(f"O título deve ter até {TAMANHO_MAXIMO_TITULO} caracteres")

    if len(descricao) > TAMANHO_MAXIMO_DESCRICAO:
        erros.append(f"A descrição deve ter até {TAMANHO_MAXIMO_DESCRICAO} caracteres")

    try:
        preco = float(preco_texto.replace(",", "."))
        if preco <= 0:
            erros.append("O preço deve ser maior que zero")
    except ValueError:
        erros.append("Informe um preço válido")

    if not id_categoria.isdigit() or int(id_categoria) not in ids_categorias:
        erros.append("Escolha uma categoria válida")

    extensao = nome_foto.rsplit(".", 1)[-1].lower() if "." in nome_foto else ""
    if extensao not in EXTENSOES_PERMITIDAS:
        erros.append("A foto deve ser JPG, JPEG, PNG ou WEBP")

    return erros


def buscar_categorias():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT ID_CATEGORIA, NOME_CATEGORIA FROM CATEGORIA ORDER BY NOME_CATEGORIA"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


@anuncio.route("/novo-anuncio", methods=["GET", "POST"])
def novo_anuncio():
    categorias = buscar_categorias()

    if request.method == "GET":
        return render_template("anuncios.html", categorias=categorias, dados={})

    titulo = request.form.get("titulo", "").strip()
    descricao = request.form.get("descricao", "").strip()
    preco_texto = request.form.get("preco", "").strip()
    id_categoria = request.form.get("categoria", "").strip()
    foto = request.files.get("foto")
    nome_foto = foto.filename if foto else ""

    ids_categorias = {c["ID_CATEGORIA"] for c in categorias}
    erros = validar_anuncio(
        titulo, descricao, preco_texto, id_categoria, nome_foto, ids_categorias
    )

    if erros:
        # Volta para o formulário mantendo o que o usuário já preencheu
        return render_template(
            "anuncios.html",
            categorias=categorias,
            erros=erros,
            dados=request.form,
        ), 422

    preco = float(preco_texto.replace(",", "."))
    id_usuario = session.get("id_usuario", ID_USUARIO_TEMPORARIO)

    # Salva a foto com um nome único em static/uploads
    extensao = nome_foto.rsplit(".", 1)[-1].lower()
    nome_arquivo = f"{uuid.uuid4().hex}.{extensao}"
    pasta_uploads = os.path.join(current_app.static_folder, "uploads")
    os.makedirs(pasta_uploads, exist_ok=True)
    caminho_foto = os.path.join(pasta_uploads, nome_arquivo)
    foto.save(caminho_foto)
    url_foto = f"/static/uploads/{nome_arquivo}"

    conexao = conectar_banco()
    cursor = conexao.cursor()
    try:
        # Anúncio e foto gravados na mesma transação (ARQUITETURA.md)
        cursor.execute(
            """
            INSERT INTO ANUNCIO
            (TITULO_ANUNCIO, DESCRICAO_ANUNCIO, PRECO_ANUNCIO, STATUS_ANUNCIO,
             ATIVO_ANUNCIO, DATA_PUBLICACAO_ANUNCIO, ID_USUARIO, ID_CATEGORIA)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                titulo,
                descricao,
                preco,
                STATUS_INICIAL,
                1,
                datetime.now(),
                id_usuario,
                int(id_categoria),
            ),
        )
        id_anuncio = cursor.lastrowid

        cursor.execute(
            "INSERT INTO FOTO (URL_FOTO, ORDEM_FOTO, ID_ANUNCIO) VALUES (%s, %s, %s)",
            (url_foto, 1, id_anuncio),
        )
        conexao.commit()

    except Exception as erro:
        conexao.rollback()
        os.remove(caminho_foto)  # a foto não fica órfã se a gravação falhar
        print("Erro ao publicar anúncio:", erro)
        return render_template(
            "anuncios.html",
            categorias=categorias,
            erros=["Não foi possível publicar o anúncio. Tente novamente."],
            dados=request.form,
        ), 500

    finally:
        cursor.close()
        conexao.close()

    produto = {
        "id": id_anuncio,
        "nome": titulo,
        "preco": preco,
        "status": STATUS_INICIAL,
        "foto": url_foto,
    }
    return render_template("sucesso_anuncio.html", produto=produto), 201
