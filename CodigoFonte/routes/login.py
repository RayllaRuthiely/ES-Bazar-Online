from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from database.db import conectar_banco

login = Blueprint("login", __name__)

@login.route("/login", methods=["GET", "POST"])
def pagina_login():
    
    if request.method == "GET":
        return render_template("login.html")

    email = request.form["email"]
    senha = request.form["senha"]

    conexao = conectar_banco()
    cursor = conexao.cursor()

    comando_sql = """
        SELECT SENHA_USUARIO
        FROM USUARIO
        WHERE EMAIL_USUARIO = %s
    """

    try:
        cursor.execute(comando_sql, (email,))
        resultado = cursor.fetchone()

        if resultado is None:
            return render_template("login.html", mensagem="Email não encontrado.")

        senha_armazenada = resultado[0]

        if check_password_hash(senha_armazenada, senha):
            return render_template("login.html", mensagem="Login bem-sucedido!")
        else:
            return render_template("login.html", mensagem="Senha incorreta.")

    except Exception as erro:
        print("Erro ao realizar login:", erro)
        return render_template("login.html", mensagem="Erro ao realizar login.")

    finally:
        cursor.close()
        conexao.close()