
from flask import Blueprint, render_template, request
from database.db import conectar_banco
from werkzeug.security import generate_password_hash

cadastro = Blueprint("cadastro", __name__)

@cadastro.route("/cadastro", methods=["GET", "POST"])


def pagina_cadastro():

    if request.method == "GET":
        return render_template("cadastro.html")

    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    telefone = request.form["telefone"]

    senha_criptografada = generate_password_hash(senha)

    conexao = conectar_banco()
    cursor = conexao.cursor()

    comando_sql = """
        INSERT INTO USUARIO
        (NOME_USUARIO, EMAIL_USUARIO, SENHA_USUARIO,
         TELEFONE_USUARIO, ATIVO_USUARIO)
        VALUES (%s, %s, %s, %s, %s)
    """

    valores = (nome,email,senha_criptografada,telefone, 1)

    try:
        cursor.execute(comando_sql, valores)
        conexao.commit()

        return render_template(
            "cadastro.html",
            mensagem="Usuário cadastrado com sucesso!"
        )

    except Exception as erro:
        conexao.rollback()
        print("Erro ao cadastrar:", erro)

        return render_template(
            "cadastro.html",
            mensagem="Não foi possível realizar o cadastro."
        )

    finally:
        cursor.close()
        conexao.close()
