from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'teste_visual'

PRODUTOS = []

@app.route('/')
def inicio():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
@app.route('/cadastro', methods=['POST'])
def ir_para_catalogo():
    return redirect(url_for('catalogo'))

@app.route('/catalogo')
def catalogo():
    busca = request.args.get('busca', '').lower()
    categoria = request.args.get('categoria', '')
    preco_faixa = request.args.get('preco', '')

    filtrados = PRODUTOS

    if busca:
        filtrados = [p for p in filtrados if busca in p['nome'].lower()]
    if categoria:
        filtrados = [p for p in filtrados if p['categoria'] == categoria]
    if preco_faixa == 'ate-30':
        filtrados = [p for p in filtrados if p['preco'] <= 30]
    elif preco_faixa == '30-60':
        filtrados = [p for p in filtrados if 30 < p['preco'] <= 60]
    elif preco_faixa == 'acima-60':
        filtrados = [p for p in filtrados if p['preco'] > 60]

    return render_template('index.html', produtos=filtrados)

@app.route('/produto/<int:id>')
def detalhe_produto(id):
    produto = next((p for p in PRODUTOS if p["id"] == id), None)
    if not produto:
        return redirect(url_for('catalogo'))
    return render_template('produto.html', produto=produto)

@app.route('/produto/<int:id>/contato', methods=['POST'])
def contato_produto(id):
    produto = next((p for p in PRODUTOS if p["id"] == id), None)
    if not produto:
        return redirect(url_for('catalogo'))

    # Regra 1: Produto reservado ou vendido
    if produto['status'] != 'Disponível':
        flash('Produto não disponível para negociação')
    # Regra 2: Vendedor sem telefone cadastrado
    elif not produto.get('contato'):
        flash('O vendedor não disponibilizou contato')

    return redirect(url_for('detalhe_produto', id=id))

@app.route('/novo-anuncio', methods=['GET', 'POST'])
def novo_anuncio():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        descricao = request.form.get('descricao', '').strip()
        preco_str = request.form.get('preco', '').strip()
        categoria = request.form.get('categoria', '').strip()

        # Validação obrigatória do protótipo
        if not titulo or not preco_str or not categoria:
            flash('Preencha os dados obrigatórios do anúncio')
            return render_template('anuncios.html')

        novo_id = len(PRODUTOS) + 1
        novo_item = {
            "id": novo_id,
            "nome": titulo,
            "descricao": descricao,
            "preco": float(preco_str),
            "categoria": categoria,
            "status": "Disponível",
            "contato": None,
            "foto": None
        }
        PRODUTOS.append(novo_item)
        
        # Abre a tela de confirmação com o card do produto criado
        return render_template('sucesso_anuncio.html', produto=novo_item)

    return render_template('anuncios.html')

@app.route('/meus-anuncios')
def meus_anuncios():
    return render_template('meus_anuncios.html', produtos=PRODUTOS)

@app.route('/alterar-status/<int:id>', methods=['POST'])
def alterar_status(id):
    novo_status = request.form.get('status')
    for produto in PRODUTOS:
        if produto["id"] == id:
            produto["status"] = novo_status
            break
    return redirect(url_for('meus_anuncios'))

@app.route('/remover-anuncio/<int:id>', methods=['POST'])
def remover_anuncio(id):
    global PRODUTOS
    PRODUTOS = [p for p in PRODUTOS if p["id"] != id]
    return redirect(url_for('meus_anuncios'))

if __name__ == '__main__':
    app.run(debug=True)






