from flask import Flask, render_template, request, redirect, url_for, flash
from routes.cadastro import cadastro
from routes.login import login
from routes.usuario import usuario
from routes.anuncio import anuncio
from routes.categoria import categoria
from routes.busca import busca
from routes.contato import contato

app = Flask(__name__)

app.register_blueprint(cadastro)
app.register_blueprint(login)
app.register_blueprint(usuario)
app.register_blueprint(anuncio)
app.register_blueprint(categoria)
app.register_blueprint(busca)
app.register_blueprint(contato)


if __name__ == "__main__":
    app.run(debug=True)




""" app.secret_key = 'teste_visual'
 """

""" PRODUTOS = [
    {
        "id": 1,
        "nome": "Produto Exemplo",
        "descricao": "Descrição de teste para visualização.",
        "preco": 50.0,
        "categoria": "Roupas",
        "status": "Disponível",
        "contato": None,
        "foto": None
    }
]


# --- MARIA EDUARDA (Catálogo e Detalhes) ---
@app.route('/catalogo')
def catalogo():
    # TODO (Maria Eduarda): Implementar filtros de busca, categoria e faixa de preço
    return render_template('index.html', produtos=PRODUTOS)

@app.route('/produto/<int:id>')
def detalhe_produto(id):
    # TODO (Maria Eduarda): Buscar o produto específico pelo ID na lista PRODUTOS
    produto = PRODUTOS[0] if PRODUTOS else None
    return render_template('produto.html', produto=produto)

@app.route('/produto/<int:id>/contato', methods=['POST'])
def contato_produto(id):
    # TODO (Maria Eduarda): Validar status do produto e contato do vendedor usando flash()
    return redirect(url_for('detalhe_produto', id=id))


# --- JOÃO GUILHERME (Criação de Anúncios) ---
@app.route('/novo-anuncio', methods=['GET', 'POST'])
def novo_anuncio():
    if request.method == 'POST':
        # TODO (João Guilherme): Pegar dados do form, validar campos obrigatórios,
        # adicionar na lista PRODUTOS e redirecionar para sucesso_anuncio.html
        pass
    return render_template('anuncios.html')


# --- SAMUEL (Gerenciamento de Anúncios) ---
@app.route('/meus-anuncios')
def meus_anuncios():
    return render_template('meus_anuncios.html', produtos=PRODUTOS)

@app.route('/alterar-status/<int:id>', methods=['POST'])
def alterar_status(id):
    # TODO (Samuel): Atualizar o status do produto (Disponível/Reservado/Vendido)
    return redirect(url_for('meus_anuncios'))

@app.route('/remover-anuncio/<int:id>', methods=['POST'])
def remover_anuncio(id):
    # TODO (Samuel): Remover o produto da lista PRODUTOS pelo ID
    return redirect(url_for('meus_anuncios'))


if __name__ == '__main__':
    app.run(debug=True)


 """




