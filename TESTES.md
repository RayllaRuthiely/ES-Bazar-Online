# Estratégia e Casos de Teste — Bazar Online

## 1. Estratégia de Teste

### 1.1 Escopo e Níveis de Teste (Modelo V)

| Nível | O que se testa | Quem escreve | Quando |
| :--- | :--- | :--- | :--- |
| **Unidade** | Regras de validação de anúncio (preço positivo, campos obrigatórios) e filtros de busca, sem servidor nem banco. | Desenvolvedor responsável pela função | Junto com a implementação |
| **Integração** | Contratos da API entre frontend e backend (rotas de cadastro/login de usuário, criação de anúncio e consulta no catálogo). | Dupla frontend e backend | Ao fechar o contrato da API |
| **Sistema** | Fluxos ponta a ponta do MVP: cadastro de usuário, publicação de anúncio, busca e visualização de contato. | Integrante que não implementou o fluxo | Antes da review da iteração |
| **Aceitação** | Validação dos critérios de aceitação (`HU-01` a `HU-08`) com o sistema em funcionamento. | Equipe e cliente/coordenação | Ao fim da iteração |

### 1.2 Ambiente, Identificação da Build e Critério de Saída

* **Ambiente de teste:** Aplicação executando em ambiente local/homologação e no pipeline de CI (GitHub Actions com Python 3.12/3.13) utilizando o cliente de testes nativo do Flask.
* **Identificação da build:** `v0.2.0-parcial` *(fluxo de cadastro e regras básicas implementados; busca e contato em construção)*.
* **Critério de saída:** Todos os casos de teste não bloqueados executados (com suíte automatizada verde no CI) e **nenhum defeito Major aberto**.

---

## 2. Omissões Deliberadas (O que não se testa)

| Fica de fora | Motivo | Risco aceito |
| :--- | :--- | :--- |
| Navegadores além das duas últimas versões do Chrome e do Firefox | A equipe e os usuários de validação utilizam esses dois navegadores principais. | Usuários em navegadores antigos ou alternativos podem enfrentar problemas visuais. |
| Testes de carga acima de 200 usuários simultâneos | O escopo do MVP local (`RE-01`) não prevê tráfego massivo nesta etapa. | O tempo de busca (`RNF-02`, até 3s) pode degradar em picos inesperados de acesso. |
| Testes automatizados de invasão e segurança avançada | Testes funcionais não garantem imunidade a ataques e a equipe não possui ferramentas especializadas. | Eventuais brechas avançadas além da proteção básica de senha (`RNF-04`) ficam descobertas nesta versão. |
| Pagamento online e cálculo de frete | Funcionalidades explicitamente fora do escopo do MVP (`RE-02` e `RE-03`). | Negociações financeiras e de entrega ocorrem fora da plataforma. |

---

## 3. Casos de Teste Derivados dos Critérios

### 3.1 Partições de Equivalência e Valores Limite

* **Preço do anúncio (`HU-02` / `CA-02.1` e `CA-02.2`):**
  * *Partição inválida:* valores negativos (ex: `-R$ 10,00`, limite `-R$ 0,01`) ou campo vazio.
  * *Partição pendente (Bloqueada):* valor zero (`R$ 0,00` — depende da pergunta **P2** sobre doações/itens gratuitos).
  * *Partição válida:* valores positivos (limite `R$ 0,01` e valor típico `R$ 50,00`).
* **Termo de busca (`HU-03` / `CA-03.1` e `CA-03.2`):**
  * *Partição válida (correspondência):* termo existente no título do anúncio (ex: `"Tênis"`).
  * *Partição válida (sem resultados):* termo inexistente no catálogo (ex: `"Geladeira Espacial"`).
  * *Partição pendente (Bloqueada):* termo presente apenas na descrição ou com diferença de acentuação (depende da pergunta **P3**).

### 3.2 Tabela de Casos de Teste e Execução

| ID | Critério | Preparo (Dado) | Passos (Quando) | Resultado Esperado (Então) | Status | Vínculo / Onde é verificado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-01.1** | `CA-01.1` | Usuário não cadastrado acessando a rota de registro. | Realizar requisição `GET /cadastro` no cliente de testes Flask. | Sistema responde com status `200 OK` exibindo o formulário de cadastro. | **Aprovado** *(Automatizado)* | `tests/test_integracao_rotas.py` (`test_rota_cadastro_exibe_formulario`). |
| **TC-01.2** | `CA-01.2` | Usuário na tela de cadastro. | Deixar campos obrigatórios em branco e clicar em confirmar. | Sistema recusa o cadastro e exibe mensagem indicando os campos obrigatórios. | Não executado *(Manual)* | Verificação manual de interface (`routes/cadastro.py`). |
| **TC-01.3** | `CA-01.2` | Usuário na tela de cadastro. | Inserir senha curta (ex: 3 caracteres) ou formato de telefone inválido. | Recusa o cadastro informando a regra de formato mínimo. | **Bloqueado** | Bloqueado pela **P1** (campos obrigatórios e tamanho mínimo de senha não definidos no `REQUISITOS.md`). |
| **TC-02.1** | `CA-02.1` | Dados válidos de título, descrição e preços positivos (`0.01` e `50.00`). | Executar a função de validação de dados do anúncio. | Validação retorna `True` (aceita valores positivos a partir do limite `0.01`). | **Aprovado** *(Automatizado)* | `tests/test_unidade_regras.py` (`test_validar_preco_anuncio_valores_limite`). |
| **TC-02.2** | `CA-02.2` | Anúncio com título vazio (`""`) e demais campos preenchidos. | Executar a função de validação de dados do anúncio. | Validação retorna `False`, recusando o anúncio sem campos obrigatórios. | **Aprovado** *(Automatizado)* | `tests/test_unidade_regras.py` (`test_recusa_anuncio_com_campos_obrigatorios_vazios`). |
| **TC-02.3** | `CA-02.2` | Anúncio com preços negativos (`-10.00` e limite `-0.01`). | Executar a função de validação de dados do anúncio. | Validação retorna `False`, recusando valores negativos. | **Aprovado** *(Automatizado)* | `tests/test_unidade_regras.py` (`test_validar_preco_anuncio_valores_limite`). |
| **TC-02.4** | `CA-02.1` | Vendedor autenticado na tela de novo anúncio. | Preencher todos os campos, informar preço `R$ 0,00` e tentar publicar. | Comportamento indefinido (aceitar como gratuito ou recusar). | **Bloqueado** | Bloqueado pela **P2** (regra para anúncios com preço `R$ 0,00` e limites de fotos em aberto). |
| **TC-03.1** | `CA-03.1` | Catálogo com anúncio ativo intitulado `"Bicicleta Aro 29"`. | Digitar `"Bicicleta"` no campo de busca e confirmar. | Sistema exibe o anúncio `"Bicicleta Aro 29"` nos resultados. | **Bloqueado** | Aguardando implementação da rota de busca (`CodigoFonte/routes/busca.py`). |
| **TC-03.2** | `CA-03.2` | Catálogo populado com produtos diversos. | Digitar `"Micro-ondas Industrial XYZ"` e confirmar a busca. | Sistema exibe mensagem informando que nenhum produto foi encontrado. | **Bloqueado** | Aguardando implementação da rota de busca (`CodigoFonte/routes/busca.py`). |
| **TC-03.3** | `CA-03.1` | Catálogo com anúncio contendo `"Palmas"` apenas na descrição (não no título). | Buscar por `"palmas"` (em minúsculo) no catálogo. | Comportamento indefinido quanto à busca na descrição e *case-sensitivity*. | **Bloqueado** | Bloqueado pela **P3** (escopo de campos da busca não especificado no `REQUISITOS.md`). |

### 3.3 Automação, Estilo e Relatório de Cobertura (Capítulo 12)

* **Comando de execução dos testes:** `pytest -v --cov=CodigoFonte --cov-report=term-missing`
* **Comandos de formatação e linter:** `ruff format --check .` e `ruff check .`
* **Integração Contínua (CI):** Executado automaticamente a cada *Pull Request* e *push* na branch `main` via `.github/workflows/verificacao.yml`.
* **Leitura do relatório de cobertura (`65%` total — 63 instruções, 22 não executadas):**
  * `CodigoFonte/app.py` atingiu **95%** de cobertura (apenas a linha `22` do bloco `if __name__ == "__main__":` fica de fora durante testes importados).
  * `CodigoFonte/routes/cadastro.py` atingiu **30%** de cobertura (coluna `Missing: 14-51`), indicando que a rota `GET` foi exercitada pelo teste automatizado, enquanto o fluxo `POST` de gravação no banco ainda aguarda implementação de dublês de conexão MySQL.
  * Os demais arquivos de rotas (`anuncio.py`, `busca.py`, `categoria.py`, `contato.py`, `login.py`, `usuario.py`) atingiram **100%** nas definições de blueprint existentes.

---

## 4. Registro do Teste de Utilidade (Validação com Usuário)

* **Data:** 18/11/2026
* **Build testada:** `v0.2.0-parcial` *(fluxo principal ainda em construção)*
* **Perfil do avaliador previsto:** Pessoa externa à equipe (aluno de outra equipe).
* **Tarefa proposta (Objetivo):** *"Acesse o Bazar Online, encontre um produto disponível para compra em Palmas–TO e descubra como entrar em contato com o vendedor para negociar."*
* **Status:** **Bloqueado** (aguardando conclusão da implementação do fluxo de busca e contato na interface).

| N.º | Observação / Situação | Classificação | Issue / Destino |
| :--- | :--- | :--- | :--- |
| — | Execução bloqueada por ausência de build com o fluxo principal (`HU-03` e `HU-04`) integrado na interface. Conforme a regra de evidência de testes, o bloqueio é registrado como ausência de evidência e não como aprovação. | **Bloqueado** | Nenhuma issue aberta até a execução na build funcional. |

