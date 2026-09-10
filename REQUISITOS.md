# Requisitos

## 1. Glossário do domínio

| Termo             | Definição                                                                                                       | Fonte |
| ----------------- | --------------------------------------------------------------------------------------------------------------- | ----- |
| Bazar Online      | Plataforma web voltada para a compra e venda de produtos entre moradores de Palmas–TO.                          | D1    |
| Usuário           | Pessoa que utiliza a plataforma para consultar ou anunciar produtos.                                            | D1    |
| Comprador         | Usuário interessado em encontrar e negociar produtos anunciados na plataforma.                                  | D1    |
| Vendedor          | Usuário que cadastra e gerencia anúncios de produtos.                                                           | D1    |
| Anúncio           | Publicação de um produto disponível para compra, contendo informações como fotos, descrição, preço e categoria. | D1    |
| Produto           | Item novo ou usado disponibilizado para venda no Bazar Online.                                                  | D1    |
| Categoria         | Classificação utilizada para organizar os produtos anunciados.                                                  | D1    |
| Catálogo          | Lista de produtos disponíveis para consulta pelos compradores.                                                  | D1    |
| Status do anúncio | Situação atual de um anúncio, podendo ser disponível, reservado ou vendido.                                     | D1    |
| Localização       | Informação utilizada para indicar que o produto está disponível na região de Palmas–TO.                         | D1    |

---

## 2. Backlog ordenado

| Ordem | Item                                 | Origem | MoSCoW | Risco | Depende de          |
| ----: | ------------------------------------ | ------ | ------ | ----- | ------------------- |
|     1 | HU-01 Cadastro e login de usuário    | D1     | Must   | Médio | —                   |
|     2 | HU-02 Cadastrar e gerenciar anúncio  | N2     | Must   | Alto  | HU-01               |
|     3 | HU-03 Buscar produtos                | N1     | Must   | Médio | HU-02               |
|     4 | HU-04 Entrar em contato com vendedor | N4     | Must   | Médio | HU-01, HU-02, HU-03 |
|     5 | HU-05 Filtrar produtos               | N3     | Should | Médio | HU-03               |
|     6 | HU-06 Gerenciar status do anúncio    | N5     | Should | Médio | HU-02               |
|     7 | HU-07 Visualizar detalhes do produto | N1     | Should | Baixo | HU-02, HU-03        |

### Classificação MoSCoW

* **Must:** requisito essencial para o MVP.
* **Should:** requisito importante, mas que pode ser desenvolvido após a fatia principal.
* **Could:** requisito desejável, mas não essencial.
* **Won't:** requisito que não será desenvolvido nesta versão.

---

## 3. Histórias de usuário e critérios de aceitação

### HU-01 — Cadastrar e gerenciar anúncio

**Como** vendedor local,
**quero** cadastrar e gerenciar anúncios de produtos,
**para** divulgar meus itens e facilitar sua venda para compradores de Palmas–TO.

**Origem:** N2, confirmada em D1.

#### CA-01.1 — Cadastro do anúncio

**Dado** que o vendedor está cadastrado no sistema,
**quando** informar as fotos, descrição, preço e categoria do produto e confirmar o cadastro,
**então** o sistema deve criar o anúncio e disponibilizá-lo no catálogo.

#### CA-01.2 — Recusa do anúncio

**Dado** que o vendedor não informou os dados necessários para o anúncio,
**quando** tentar publicá-lo,
**então** o sistema deve recusar o cadastro e informar que os dados obrigatórios precisam ser preenchidos.

#### CA-01.3 — Efeito persistente

**Dado** que o anúncio foi cadastrado com sucesso,
**quando** o vendedor ou outro usuário consultar novamente o catálogo,
**então** o anúncio deve permanecer disponível até que seja alterado, removido ou tenha seu status modificado.

---

### HU-02 — Buscar produtos

**Como** comprador local,
**quero** pesquisar produtos disponíveis,
**para** encontrar itens de meu interesse em Palmas–TO.

**Origem:** N1, confirmada em D1.

#### CA-02.1 — Produto encontrado

**Dado** que existem produtos cadastrados no sistema,
**quando** o comprador realizar uma busca por um produto,
**então** o sistema deve apresentar os anúncios correspondentes à pesquisa.

#### CA-02.2 — Nenhum produto encontrado

**Dado** que não existem anúncios correspondentes à pesquisa,
**quando** o comprador realizar a busca,
**então** o sistema deve informar que nenhum produto foi encontrado.

#### CA-02.3 — Efeito persistente

**Dado** que existem anúncios cadastrados,
**quando** o comprador realizar uma nova busca,
**então** os anúncios que continuam disponíveis devem permanecer consultáveis no catálogo.

---

### HU-03 — Entrar em contato com o vendedor

**Como** comprador local,
**quero** entrar em contato diretamente com o vendedor,
**para** negociar o produto e combinar a retirada e o pagamento.

**Origem:** N4, confirmada em D1.

#### CA-03.1 — Contato disponível

**Dado** que o comprador visualizou um anúncio disponível,
**quando** selecionar a opção de contato,
**então** o sistema deve apresentar a forma de contato disponibilizada pelo vendedor.

#### CA-03.2 — Contato indisponível

**Dado** que o vendedor não disponibilizou uma forma de contato,
**quando** o comprador tentar entrar em contato,
**então** o sistema deve informar que não há uma forma de contato disponível.

#### CA-03.3 — Efeito persistente

**Dado** que o vendedor possui uma forma de contato cadastrada,
**quando** o anúncio for consultado novamente enquanto estiver disponível,
**então** a forma de contato deve continuar disponível ao comprador.

---

### HU-04 — Filtrar produtos

**Como** comprador local,
**quero** filtrar produtos por categoria e faixa de preço,
**para** encontrar mais facilmente os itens que correspondem ao que procuro.

**Origem:** N3, confirmada em D1.

#### CA-04.1 — Filtro aplicado

**Dado** que existem produtos de diferentes categorias e preços,
**quando** o comprador selecionar uma categoria ou faixa de preço,
**então** o sistema deve apresentar somente os produtos correspondentes ao filtro.

#### CA-04.2 — Nenhum resultado

**Dado** que não existem produtos correspondentes ao filtro selecionado,
**quando** o comprador aplicar o filtro,
**então** o sistema deve informar que nenhum produto foi encontrado.

#### CA-04.3 — Remoção do filtro

**Dado** que um filtro está aplicado,
**quando** o comprador removê-lo,
**então** o sistema deve voltar a apresentar os produtos disponíveis sem aquele filtro.

---

### HU-05 — Gerenciar status do anúncio

**Como** vendedor,
**quero** alterar o status do meu anúncio,
**para** informar se o produto está disponível, reservado ou vendido.

**Origem:** N5, confirmada em D1.

#### CA-05.1 — Alteração de status

**Dado** que o vendedor possui um anúncio cadastrado,
**quando** alterar seu status,
**então** o sistema deve atualizar o anúncio para o status selecionado.

#### CA-05.2 — Status inválido

**Dado** que o vendedor está alterando o status do anúncio,
**quando** informar um status diferente dos estados permitidos,
**então** o sistema deve recusar a alteração.

#### CA-05.3 — Efeito persistente

**Dado** que o status do anúncio foi alterado,
**quando** o anúncio for consultado novamente,
**então** o sistema deve apresentar o status atualizado.

---

### HU-06 — Cadastro e login de usuário

**Como** usuário,
**quero** criar uma conta e realizar login,
**para** acessar as funcionalidades destinadas aos usuários cadastrados.

**Origem:** D1.

#### CA-06.1 — Cadastro realizado

**Dado** que o usuário informou os dados necessários,
**quando** confirmar o cadastro,
**então** o sistema deve registrar a conta.

#### CA-06.2 — Cadastro recusado

**Dado** que os dados obrigatórios não foram preenchidos corretamente,
**quando** o usuário tentar concluir o cadastro,
**então** o sistema deve recusar a operação e informar o problema.

#### CA-06.3 — Efeito persistente

**Dado** que o cadastro foi concluído,
**quando** o usuário acessar novamente o sistema,
**então** sua conta deve continuar registrada.

---

### HU-07 — Visualizar detalhes do produto

**Como** comprador,
**quero** visualizar os detalhes de um produto,
**para** avaliar o item antes de entrar em contato com o vendedor.

**Origem:** N1, confirmada em D1.

#### CA-07.1 — Detalhes exibidos

**Dado** que existe um anúncio disponível,
**quando** o comprador selecionar o produto,
**então** o sistema deve apresentar suas informações, incluindo fotos, descrição, preço e categoria.

#### CA-07.2 — Anúncio indisponível

**Dado** que o anúncio não está mais disponível,
**quando** o comprador tentar acessá-lo,
**então** o sistema deve informar que o produto não está disponível para negociação.

#### CA-07.3 — Informações atualizadas

**Dado** que o vendedor alterou as informações do anúncio,
**quando** o comprador acessar novamente o produto,
**então** o sistema deve apresentar as informações atualizadas.

---

## 4. Casos de uso

### UC-01 — Publicar anúncio

**Ator principal:** Vendedor

#### Fluxo principal

1. O vendedor acessa a opção de cadastrar anúncio.
2. O sistema apresenta o formulário.
3. O vendedor informa fotos, descrição, preço e categoria.
4. O vendedor confirma o cadastro.
5. O sistema valida as informações.
6. O sistema registra o anúncio.
7. O sistema disponibiliza o anúncio no catálogo.
8. O sistema informa que o anúncio foi cadastrado com sucesso.

#### Fluxos alternativos

* **A1 — Dados incompletos:** caso algum dado obrigatório não seja informado, o sistema solicita seu preenchimento.
* **A2 — Dados inválidos:** caso alguma informação seja inválida, o sistema informa o erro e não publica o anúncio.
* **A3 — Cancelamento:** caso o vendedor cancele a operação, o anúncio não deve ser cadastrado.

---

### UC-02 — Buscar produto

**Ator principal:** Comprador

#### Fluxo principal

1. O comprador acessa o catálogo.
2. O comprador informa uma palavra-chave ou realiza uma consulta.
3. O sistema processa a busca.
4. O sistema apresenta os anúncios correspondentes.
5. O comprador seleciona um anúncio.
6. O sistema apresenta os detalhes do produto.

#### Fluxos alternativos

* **A1 — Nenhum resultado:** caso nenhum anúncio corresponda à busca, o sistema informa que nenhum produto foi encontrado.
* **A2 — Filtro:** o comprador pode aplicar filtros por categoria e faixa de preço.
* **A3 — Nova busca:** o comprador pode realizar uma nova pesquisa.

---

### UC-03 — Entrar em contato com o vendedor

**Ator principal:** Comprador

#### Fluxo principal

1. O comprador acessa um anúncio.
2. O sistema apresenta as informações do produto.
3. O comprador seleciona a opção de contato.
4. O sistema apresenta a forma de contato disponibilizada pelo vendedor.
5. O comprador utiliza o canal informado para iniciar a negociação.
6. Comprador e vendedor combinam a retirada e o pagamento.

#### Fluxos alternativos

* **A1 — Contato não informado:** caso o vendedor não tenha disponibilizado uma forma de contato, o sistema informa que não há contato disponível.
* **A2 — Anúncio indisponível:** caso o produto esteja vendido ou indisponível, o sistema informa que a negociação não está disponível.

---

### UC-04 — Gerenciar anúncio

**Ator principal:** Vendedor

#### Fluxo principal

1. O vendedor acessa seus anúncios.
2. O sistema apresenta os anúncios cadastrados.
3. O vendedor seleciona um anúncio.
4. O vendedor escolhe alterar, remover ou modificar seu status.
5. O sistema executa a operação escolhida.
6. O sistema apresenta o estado atualizado do anúncio.

#### Fluxos alternativos

* **A1 — Anúncio não encontrado:** caso o anúncio não seja encontrado, o sistema informa que ele não está disponível.
* **A2 — Cancelamento:** caso o vendedor cancele a operação, nenhuma alteração deve ser realizada.

---

## 5. Requisitos não funcionais

| Código | Requisito                                                        | Grandeza        | Condição                                    | Valor aceitável                                                                | Como verificar                        |
| ------ | ---------------------------------------------------------------- | --------------- | ------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------- |
| RNF-01 | A plataforma deve apresentar uma interface simples e organizada. | Usabilidade     | Usuário realizando tarefas do MVP.          | As funcionalidades principais devem ser identificadas sem orientação externa.  | Teste de usabilidade com usuários.    |
| RNF-02 | A busca deve apresentar os resultados em tempo adequado.         | Desempenho      | Usuário realiza uma busca no catálogo.      | Resultados apresentados em até 3 segundos em condições normais.                | Teste de tempo de resposta.           |
| RNF-03 | A plataforma deve funcionar em diferentes tamanhos de tela.      | Compatibilidade | Acesso por computador ou dispositivo móvel. | Funcionalidades principais disponíveis sem perda significativa de usabilidade. | Teste em diferentes tamanhos de tela. |
| RNF-04 | Os dados de acesso dos usuários devem ser protegidos.            | Segurança       | Cadastro e autenticação de usuários.        | Senhas não devem ser armazenadas em texto simples.                             | Inspeção da implementação.            |
| RNF-05 | A plataforma deve manter os anúncios e seus dados atualizados.   | Confiabilidade  | Alteração ou remoção de anúncios.           | Alterações devem ser refletidas nas consultas posteriores.                     | Testes funcionais.                    |

---

## 6. Restrições e regras de negócio

### 6.1 Restrições

#### RE-01 — Área de atuação

O sistema será destinado à compra e venda local entre moradores de **Palmas–TO**.

**Origem:** D1.

#### RE-02 — Pagamento

O sistema não realizará pagamentos online. O pagamento será combinado diretamente entre comprador e vendedor.

**Origem:** D1.

#### RE-03 — Entrega

O sistema não realizará cálculo automático de frete. A entrega ou retirada deverá ser combinada diretamente entre comprador e vendedor.

**Origem:** D1.

#### RE-04 — Comunicação

O sistema não possuirá chat em tempo real nesta versão. O contato inicial será realizado por meio de canais externos disponibilizados pelo vendedor.

**Origem:** D1.

#### RE-05 — Avaliações

O sistema não possuirá avaliação de usuários nesta versão do projeto.

**Origem:** D1.

### 6.2 Regras de negócio

#### RN-01 — Tipos de produtos

A plataforma permitirá anúncios de produtos novos ou usados, incluindo roupas, calçados, acessórios e outros itens compatíveis com a proposta do bazar.

**Origem:** D1.

#### RN-02 — Status dos anúncios

Um anúncio poderá possuir os seguintes status:

* **Disponível**
* **Reservado**
* **Vendido**

**Origem:** N5, D1.

#### RN-03 — Anúncios vendidos

Um anúncio marcado como **Vendido** não deverá ser apresentado como disponível para negociação.

**Origem:** N5, D1.

#### RN-04 — Responsabilidade pelas informações

O vendedor será responsável pelas informações apresentadas em seu anúncio, incluindo descrição, preço, fotos e demais informações fornecidas.

**Origem:** D1.

#### RN-05 — Comércio local

Os anúncios deverão estar relacionados à negociação na região de Palmas–TO, de acordo com o escopo definido para o projeto.

**Origem:** D1.

---

## 7. Validações realizadas

### V1 — 2026-09-01 — Validação do escopo e MVP

A equipe revisou as necessidades, cenários e escopo definidos durante a descoberta do problema.

| Achado                                                              | Efeito                                                                           | Item alterado |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------- |
| A busca por produtos é uma necessidade principal dos compradores.   | A busca foi colocada entre as primeiras funcionalidades do backlog.              | HU-02         |
| Os vendedores precisam cadastrar e gerenciar seus anúncios.         | O cadastro e gerenciamento de anúncios foi definido como parte principal do MVP. | HU-01         |
| O contato direto é necessário para concluir a negociação.           | A funcionalidade de contato foi incluída entre as três primeiras histórias.      | HU-03         |
| Os compradores precisam encontrar produtos por categorias e preços. | Foram definidos filtros por categoria e faixa de preço.                          | HU-04         |
| Os anúncios precisam informar sua situação atual.                   | Foram definidos os status disponível, reservado e vendido.                       | HU-05         |
| O sistema não realizará pagamento online.                           | Pagamentos foram mantidos fora do escopo desta versão.                           | RE-02         |
| O sistema não terá chat em tempo real.                              | O contato inicial será realizado por canal externo.                              | RE-04         |
| O projeto será direcionado para Palmas–TO.                          | A área de atuação foi definida como uma restrição do sistema.                    | RE-01         |

---

## 8. Relação entre necessidades e requisitos

| Necessidade | Descrição                                                                  | Requisitos relacionados |
| ----------- | -------------------------------------------------------------------------- | ----------------------- |
| N1          | Visualizar catálogo de produtos disponíveis na região                      | HU-02, HU-07            |
| N2          | Cadastrar e gerenciar anúncios de itens usados com fotos e descrição       | HU-01, HU-06            |
| N3          | Filtrar produtos por categorias e faixas de preço                          | HU-04                   |
| N4          | Entrar em contato direto com o vendedor para negociar e combinar a entrega | HU-03                   |
| N5          | Controlar o status dos anúncios                                            | HU-05                   |

---

## 9. Histórico de revisão

| Data       | Versão | Alteração                                                                                                                                                                                    |
| ---------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-10 | 1.0    | Criação do documento de requisitos com glossário, backlog, histórias de usuário, critérios de aceitação, casos de uso, requisitos não funcionais, restrições, regras de negócio e validação. |
| 2026-09-10 | 1.1    | Adequação dos requisitos ao escopo definido na `DESCOBERTA.md` e ao MVP do projeto.                                                                                                          |
