from flask import Blueprint, render_template, request
from database.db import conectar_banco
from werkzeug.security import generate_password_hash

categoria = Blueprint("categoria", __name__)