from database.db import conectar_banco
from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.security import check_password_hash

login = Blueprint("login", __name__)


@login.route("/login", methods=["GET", "POST"])
def pagina_login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    senha = request.form["senha"]

    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    comando_sql = """
        SELECT ID_USUARIO, NOME_USUARIO, SENHA_USUARIO
        FROM USUARIO
        WHERE EMAIL_USUARIO = %s
    """

    try:
        cursor.execute(comando_sql, (email,))
        usuario = cursor.fetchone()

        if usuario is None:
            return render_template("login.html", mensagem="Email não encontrado.")

        senha_armazenada = usuario["SENHA_USUARIO"]

        if check_password_hash(senha_armazenada, senha):

            session.clear()

            session["id_usuario"] = usuario["ID_USUARIO"]
            session["nome_usuario"] = usuario["NOME_USUARIO"]


            return redirect(url_for("anuncio.novo_anuncio"))
    
        else:
            return render_template( "login.html", mensagem="Senha incorreta.")

    
    except Exception as erro:
        print("Erro ao realizar login:", erro)
        return render_template("login.html", mensagem="Erro ao realizar login.")

    finally:
        cursor.close()
        conexao.close()
