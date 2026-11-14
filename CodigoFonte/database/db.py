
import mysql.connector

def conectar_banco():
    conexao = mysql.connector.connect(

        host="0000",
        port="0000",
        user="0000",
        password="0000",
        database="0000"
    )

    return conexao