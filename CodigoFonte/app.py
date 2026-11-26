import os

from flask import Flask, redirect, url_for
from routes.anuncio import anuncio
from routes.busca import busca
from routes.cadastro import cadastro
from routes.categoria import categoria
from routes.contato import contato
from routes.login import login
from routes.usuario import usuario

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "chave-desenvolvimento-bazar")

app.register_blueprint(cadastro)
app.register_blueprint(login)
app.register_blueprint(usuario)
app.register_blueprint(anuncio)
app.register_blueprint(categoria)
app.register_blueprint(busca)
app.register_blueprint(contato)


@app.route("/")
def inicio():
    return redirect(url_for("cadastro.pagina_cadastro"))


if __name__ == "__main__":
    app.run(debug=True)
