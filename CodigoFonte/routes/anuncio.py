from flask import Blueprint, render_template, request
from database.db import conectar_banco
from werkzeug.security import generate_password_hash

anuncio = Blueprint("anuncio", __name__)