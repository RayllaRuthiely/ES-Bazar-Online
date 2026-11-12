import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="://aivencloud.com",
        port=SUA_PORTA_AIVEN, # Coloque o número sem aspas (ex: 15432)
        user="avnadmin",
        password="SUA_SENHA_AQUI",
        database="BAZAR_ONLINE"
    )

# Teste rápido de conexão (apague estas duas linhas depois de testar)
if __name__ == "__main__":
    conexao = conectar()
    print("Conectado com sucesso!", conexao.is_connected())
    conexao.close()
