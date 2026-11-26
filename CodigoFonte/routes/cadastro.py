from database.db import conectar_banco
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("cadastro.html")


@app.route("/cadastro", methods=["POST"])
def cadastrar_usuario():

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

    valores = (nome, email, senha_criptografada, telefone, 1)

    cursor.execute(comando_sql, valores)

    conexao.commit()
    cursor.close()
    conexao.close()

    return render_template("cadastro.html", mensagem="Usuário cadastrado com sucesso!")


if __name__ == "__main__":
    app.run(debug=True)
