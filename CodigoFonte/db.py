import mysql.connector

def conectar():
    # TODO (Alana): Preencher com os dados reais do servidor Aiven (sem subir senhas reais no Git público)
    return mysql.connector.connect(
        host="SEU_HOST_AIVEN.aivencloud.com",
        port=00000, # Coloque o número da porta sem aspas
        user="avnadmin",
        password="SUA_SENHA_AQUI",
        database="BAZAR_ONLINE"
    )

# ==========================================================
# TODO (Alana): Criar abaixo as funções de banco de dados
# ==========================================================

# 1. Usuários (para integrar com cadastro.html e app.py):
#    - criar_usuario(nome, email, senha, contato)
#    - buscar_usuario_por_email(email)

# 2. Produtos (para substituir a lista PRODUTOS do app.py):
#    - listar_produtos()
#    - inserir_produto(titulo, descricao, preco, categoria, foto)
#    - atualizar_status_produto(id_produto, novo_status)
#    - deletar_produto(id_produto)

