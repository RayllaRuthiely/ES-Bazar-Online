import os

import mysql.connector
from dotenv import load_dotenv

# Lê as variáveis do arquivo .env (que não vai para o GitHub)
load_dotenv()


def conectar_banco():
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "BAZAR_ONLINE"),
    )

    return conexao
