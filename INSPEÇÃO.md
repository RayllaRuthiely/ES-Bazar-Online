# Inspeção de Requisitos — Bazar Online

## 1. Identificação

* **Projeto:** Bazar Online
* **Documento inspecionado:** `REQUISITOS.md`
* **Atividade:** Verificação e Validação (Capítulo 11)
* **Data:** 18/11/2026
* **Versão do documento:** 1.4

## 2. Participantes e papéis

| Integrante | Papel | Responsabilidade na inspeção |
| :--- | :--- | :--- |
| Alana Farias Silva | Moderadora | Conduz a reunião, verifica a preparação individual e confere as correções no retrabalho. |
| Raylla Ruthiely Gomes Santana | Autora | Esclarece dúvidas sobre o texto original e aplica as correções/perguntas no `REQUISITOS.md`. |
| Samuel Felipe De Sena Estevão | Leitor | Parafraseia os requisitos em voz alta para evidenciar lacunas e interpretações ambíguas. |
| João Guilherme Aguiar Lustosa | Testador | Avalia se os requisitos e critérios permitem derivar casos de teste verificáveis. |
| Maria Eduarda Rodrigues Lima | Registradora | Documenta cada achado com localização, característica violada, gravidade e encaminhamento. |

## 3. Itens selecionados para inspeção

* **HU-01** — Cadastro e login de usuário.
* **HU-02** — Cadastrar e gerenciar anúncio.
* **HU-03** — Buscar produtos.
* **CA-02.2** — Recusa do anúncio.
* **CA-03.1** — Produto encontrado.

## 4. Objetivo

Verificar a qualidade técnica dos requisitos selecionados antes e durante a construção dos casos de teste, identificando problemas de completude, consistência, não ambiguidade e verificabilidade, sem depender ainda da validação externa com o cliente.

## 5. Registro dos achados

**Status:** Concluída em 18/11/2026.

| N.º | Local | Achado | Característica violada | Gravidade | Decisão / Encaminhamento |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | **HU-01** (`CA-01.1` e `CA-01.2`) | O texto menciona "dados necessários" e "dados obrigatórios", mas não lista quais campos compõem o cadastro (ex: nome, e-mail, senha, telefone/WhatsApp) nem o tamanho mínimo da senha. | Completo / Não ambíguo | **Major** | Abrir pergunta **P1** no `REQUISITOS.md` e marcar casos de teste de validação de formato/senha como **Bloqueado** no `TESTES.md`. |
| **2** | **HU-01** | A história pede "criar uma conta e realizar login", mas os três critérios (`CA-01.1` a `CA-01.3`) cobrem apenas o cadastro, deixando o fluxo e as falhas de login sem critério de aceitação. | Completo | **Major** | Retrabalho da Autora: incluir critérios específicos para login válido (`CA-01.4`) e login recusado (`CA-01.5`) no `REQUISITOS.md`. |
| **3** | **HU-02** e **`CA-02.2`** | O critério recusa o anúncio se faltar "dados necessários", mas não especifica limites de validação: quantidade mínima/máxima de fotos, formatos aceitos, tamanho em MB e se o preço pode ser R$ 0,00. | Verificável / Completo | **Major** | Abrir pergunta **P2** no `REQUISITOS.md` sobre regras de fotos e preço; marcar casos de teste de valor limite como **Bloqueado** no `TESTES.md`. |
| **4** | **HU-02** | O título da história inclui "gerenciar anúncio" (editar/atualizar), mas os critérios (`CA-02.1` a `CA-02.3`) tratam apenas da criação e publicação. | Completo | **Minor** | Retrabalho da Autora: ajustar o título de `HU-02` para "Cadastrar anúncio" (visto que status e remoção estão em `HU-06` e `HU-08`) ou adicionar critério de edição. |
| **5** | **HU-03** e **`CA-03.1`** | "Apresentar os anúncios correspondentes à pesquisa" não define onde a busca atua (apenas no título, na descrição ou em ambos) nem se diferencia maiúsculas/minúsculas ou acentos. | Não ambíguo / Verificável | **Major** | Abrir pergunta **P3** no `REQUISITOS.md` para definir o escopo da busca por palavra-chave e bloquear o caso `TC-03.3`. |

## 6. Perguntas em aberto geradas para o `REQUISITOS.md`

* **P1 (sobre HU-01):** Quais são exatamente os campos obrigatórios no cadastro de usuário (nome, e-mail, senha, WhatsApp/telefone) e qual a regra mínima de segurança para a senha?
* **P2 (sobre HU-02 / CA-02.2):** Qual a quantidade mínima e máxima de fotos por anúncio, quais formatos de imagem são aceitos (ex: JPG, PNG) e o sistema permite cadastrar anúncios gratuitos com preço igual a `R$ 0,00`?
* **P3 (sobre HU-03 / CA-03.1):** A busca por palavra-chave deve pesquisar apenas no título do anúncio ou também na descrição, e deve ignorar diferenças entre letras maiúsculas, minúsculas e acentos?

## 7. Melhoria do processo e acompanhamento

* **Melhoria identificada (causa comum):** Os achados 1, 3 e 5 ocorreram porque os critérios de aceitação usaram termos genéricos ("dados necessários", "correspondentes") sem especificar os limites de entrada. A equipe passa a adotar na revisão de requisitos a pergunta-guia: *"Quais são os valores mínimos, máximos e formatos inválidos para cada campo citado?"*
* **Acompanhamento:** Após a Autora (Raylla) atualizar o `REQUISITOS.md` com as correções Minor e as perguntas P1, P2 e P3, a Moderadora (Alana) confere a atualização antes do fechamento do ciclo.
